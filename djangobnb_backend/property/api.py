from django.http import JsonResponse
from rest_framework.decorators import (
    api_view,
    permission_classes,
    authentication_classes,
)
from django.core.paginator import Paginator

from rest_framework_simplejwt.tokens import AccessToken
from .forms import PropertyForm
from .models import Property, Reservation
from .serializers import (
    PropertiesListSerializer,
    PropertiesDetailSerializer,
    ReservationListSerializer,
)
from useraccount.models import User
import stripe
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt


@api_view(["GET"])
@authentication_classes([])
@permission_classes([])
def properties_list(request):

    try:
        token = request.META.get("HTTP_AUTHORIZATION").split("Bearer ")[1]
        token = AccessToken(token)
        user_id = token.payload["user_id"]
        user = User.objects.get(pk=user_id)

    except Exception as e:
        user = None

    favorites = []
    properties = Property.objects.all().order_by("-created_at")

    is_favorites = request.GET.get("is_favorites", "")
    landlord_id = request.GET.get("landlord_id", "")
    country = request.GET.get("country", "")
    category = request.GET.get("category", "")
    checkin_date = request.GET.get("checkIn", "")
    checkout_date = request.GET.get("checkOut", "")
    bedrooms = request.GET.get("numBedrooms", "")
    bathrooms = request.GET.get("numBathrooms", "")
    guests = request.GET.get("numGuests", "")

    if checkin_date and checkout_date:
        exact_matches = Reservation.objects.filter(
            start_date=checkin_date
        ) | Reservation.objects.filter(end_date=checkout_date)
        overlap_matches = Reservation.objects.filter(
            start_date__lte=checkout_date, end_date__gte=checkin_date
        )
        all_matches = []

        for reservation in exact_matches | overlap_matches:
            all_matches.append(reservation.property_id)

        properties = properties.exclude(id__in=all_matches)

    if landlord_id:
        properties = properties.filter(landlord_id=landlord_id)

    if is_favorites:
        properties = properties.filter(favorited__in=[user])

    if guests:
        properties = properties.filter(guests__gte=guests)

    if bedrooms:
        properties = properties.filter(bedrooms__gte=bedrooms)

    if bathrooms:
        properties = properties.filter(bathrooms__gte=bathrooms)

    if country:
        properties = properties.filter(country=country)

    if category and category != "undefined":
        properties = properties.filter(category=category)

    if user:
        for property in properties:
            if user in property.favorited.all():
                favorites.append(property.id)

    page = request.GET.get("page", 1)
    limit = request.GET.get("limit", 10)
    paginator = Paginator(properties, limit)
    paginated_properties = paginator.get_page(page)

    serializer = PropertiesListSerializer(paginated_properties, many=True)
    return JsonResponse(
        {
            "data": serializer.data,
            "favorites": favorites,
            "totalPages": paginator.num_pages,
            "current_page": paginated_properties.number,
        }
    )


@api_view(["GET"])
@authentication_classes([])
@permission_classes([])
def properties_detail(request, pk):
    property = Property.objects.get(pk=pk)
    serializer = PropertiesDetailSerializer(property, many=False)

    return JsonResponse(serializer.data)


@api_view(["GET"])
@authentication_classes([])
@permission_classes([])
def property_reservations(request, pk):
    property = Property.objects.get(pk=pk)
    reservations = property.reservation.all()
    serializer = ReservationListSerializer(reservations, many=True)

    return JsonResponse(serializer.data, safe=False)


@api_view(["DELETE"])
@authentication_classes([])
@permission_classes([])
def delete_reservation(request, pk):
    try:
        reservation = Reservation.objects.get(pk=pk)
    except Reservation.DoesNotExist:
        return JsonResponse(
            {"success": False, "message": "Reservation not found"}, status=404
        )

    if request.method == "DELETE":
        reservation.delete()
        return JsonResponse({"success": True}, status=200)
    else:
        return JsonResponse(
            {"success": False, "message": "Invalid request method"}, status=400
        )


stripe.api_key = settings.STRIPE_SECRET_KEY


@api_view(["POST"])
@authentication_classes([])
@permission_classes([])
@csrf_exempt
def confirm_payment(request, pk):
    try:
        reservation = Reservation.objects.get(pk=pk)
        payment_intent_id = request.data.get("payment_intent_id")

        intent = stripe.PaymentIntent.retrieve(payment_intent_id)

        if intent.status == "succeeded":
            reservation.status = "confirmed"
            reservation.save()

            return JsonResponse(
                {
                    "success": True,
                    "reservation": ReservationListSerializer(reservation).data,
                }
            )
        else:
            return JsonResponse(
                {"success": False, "message": "Payment not successful"}, status=400
            )
    except Reservation.DoesNotExist:
        return JsonResponse({"error": "Reservation not found"}, status=404)
    except Exception as e:
        print(f"Error confirming Payment Intent: {str(e)}")
        return JsonResponse({"error": str(e)}, status=500)


stripe.api_key = settings.STRIPE_SECRET_KEY


@api_view(["POST"])
@authentication_classes([])
@permission_classes([])
@csrf_exempt
def payment_intent(request, pk):
    try:
        reservation = Reservation.objects.get(pk=pk)
        amount = int(reservation.total_price * 100)

        intent = stripe.PaymentIntent.create(
            amount=amount,
            currency="eur",
            metadata={"reservation_id": reservation.id},
        )

        return JsonResponse(
            {
                "success": True,
                "client_secret": intent["client_secret"],
                "reservation": ReservationListSerializer(reservation).data,
            }
        )
    except Reservation.DoesNotExist:
        return JsonResponse({"error": "Reservation not found"}, status=404)
    except Exception as e:
        print(f"Error creating Payment Intent: {str(e)}")
        return JsonResponse({"error": str(e)}, status=500)


@api_view(["POST", "FILES"])
def create_property(request):
    form = PropertyForm(request.POST, request.FILES)
    if form.is_valid():
        property = form.save(commit=False)
        property.landlord = request.user
        property.save()

        return JsonResponse({"success": True})
    else:
        print("error", form.errors, form.non_field_errors)
        return JsonResponse({"errors": form.errors.as_json()}, status=400)


@api_view(["PUT"])
@authentication_classes([])
@permission_classes([])
def update_property(request, pk):
    try:
        property = Property.objects.get(pk=pk)
    except Property.DoesNotExist:
        return JsonResponse({"errors": "Property not found"}, status=404)

    form = PropertyForm(request.data, request.FILES, instance=property)
    if form.is_valid():
        form.save()
        return JsonResponse({"success": True})
    else:
        return JsonResponse({"errors": form.errors.as_json()}, status=400)


@api_view(["DELETE"])
@authentication_classes([])
@permission_classes([])
def delete_property(request, pk):
    try:
        property = Property.objects.get(pk=pk)
    except Property.DoesNotExist:
        return JsonResponse(status=404)

    if request.method == "DELETE":
        property.delete()
        return JsonResponse({"success": True}, status=200)
    else:
        return JsonResponse(status=400)


@api_view(["POST"])
def book_property(request, pk):
    try:
        start_date = request.POST.get("start_date", "")
        end_date = request.POST.get("end_date", "")
        number_of_nights = request.POST.get("number_of_nights", "")
        total_price = request.POST.get("total_price", "")
        guests = request.POST.get("guests", "")

        property = Property.objects.get(pk=pk)

        Reservation.objects.create(
            property=property,
            start_date=start_date,
            end_date=end_date,
            number_of_nights=number_of_nights,
            total_price=total_price,
            guests=guests,
            created_by=request.user,
        )

        return JsonResponse({"success": True})

    except Exception as e:
        print("error", e)

        return JsonResponse({"success": False})


@api_view(["POST"])
def toggle_favorite(request, pk):
    property = Property.objects.get(pk=pk)

    if request.user in property.favorited.all():
        property.favorited.remove(request.user)

        return JsonResponse({"is_favorite": False})
    else:

        property.favorited.add(request.user)

        return JsonResponse({"is_favorite": True})
