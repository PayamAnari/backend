from django.http import JsonResponse
from rest_framework.decorators import (
    api_view,
    permission_classes,
    authentication_classes,
)
from .models import Review
from .serializer import ReviewSerializer
from .form import ReviewForm
from property.models import Property
from django.db.models import Avg


@api_view(["GET"])
@permission_classes([])
@authentication_classes([])
def get_reviews(request, property_id):
    reviews = Review.objects.filter(property_id=property_id)
    serializer = ReviewSerializer(reviews, many=True)

    average_rating = reviews.aggregate(Avg("rating"))["rating__avg"]
    if average_rating is not None:
        average_rating = format(average_rating, ".2f")

    response_data = {"reviews": serializer.data, "average_rating": average_rating}

    return JsonResponse(response_data, safe=False)


@api_view(["POST"])
def create_review(request, property_id):
    try:
        property = Property.objects.get(id=property_id)
    except Property.DoesNotExist:
        return JsonResponse({"error": "Property not found"}, status=404)

    form = ReviewForm(request.POST)
    if form.is_valid():
        review = form.save(commit=False)
        review.property = property
        review.user = request.user
        review.save()

        return JsonResponse({"success": True}, status=201)
    else:
        return JsonResponse({"errors": form.errors.as_json()}, status=400)


@api_view(["DELETE"])
def delete_review(request, review_id):
    try:
        review = Review.objects.get(id=review_id)
    except Review.DoesNotExist:
        return JsonResponse({"error": "Review not found"}, status=404)

    review.delete()
    return JsonResponse({"success": True}, status=200)
