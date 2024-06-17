from .models import User
from .serializers import UserDetailSerializer, ProfilePhotoSerializer
from rest_framework.decorators import (
    api_view,
    authentication_classes,
    permission_classes,
)
from django.http import JsonResponse
from rest_framework import status
from property.serializers import ReservationListSerializer
from rest_framework.permissions import IsAuthenticated
from django.conf import settings


@api_view(["GET"])
@authentication_classes([])
@permission_classes([])
def landlord_detail(request, pk):
    user = User.objects.get(pk=pk)
    serializer = UserDetailSerializer(user, many=False)

    return JsonResponse(serializer.data, safe=False)


@api_view(["GET"])
def reservations_list(request):
    reservations = request.user.reservation.all()
    serializers = ReservationListSerializer(reservations, many=True)

    return JsonResponse(serializers.data, safe=False)


@api_view(["POST"])
@authentication_classes([])
@permission_classes([])
def upload_profile(request, pk):
    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return JsonResponse(
            {"error": "User not found"}, status=status.HTTP_404_NOT_FOUND
        )

    serializer = ProfilePhotoSerializer(user, data=request.data)
    if serializer.is_valid():
        serializer.save()
        avatar_url = f"{settings.WEBSITE_URL}{user.avatar.url}"
        return JsonResponse({"avatar_url": avatar_url}, status=status.HTTP_201_CREATED)
    return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["PUT"])
@permission_classes([IsAuthenticated])
def update_landlord(request, pk):
    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return JsonResponse(
            {"error": "User not found"}, status=status.HTTP_404_NOT_FOUND
        )

    if not request.user.is_authenticated:
        return JsonResponse(
            {"error": "User not authenticated"}, status=status.HTTP_401_UNAUTHORIZED
        )

    if request.user.id != user.id:
        return JsonResponse(
            {"error": "You can only update your own profile"},
            status=status.HTTP_403_FORBIDDEN,
        )

    serializer = UserDetailSerializer(user, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data)
    return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["DELETE"])
@permission_classes([IsAuthenticated])
def update_landlord(request, pk):
    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return JsonResponse(
            {"error": "User not found"}, status=status.HTTP_404_NOT_FOUND
        )

    if not request.user.is_authenticated:
        return JsonResponse(
            {"error": "User not authenticated"}, status=status.HTTP_401_UNAUTHORIZED
        )

    if request.user.id != user.id:
        return JsonResponse(
            {"error": "You can only delete your own profile"},
            status=status.HTTP_403_FORBIDDEN,
        )

    user.delete()
    return JsonResponse({"message": "User deleted"}, status=status.HTTP_204_NO_CONTENT)
