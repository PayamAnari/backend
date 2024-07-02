from django.http import JsonResponse
from rest_framework.decorators import (
    api_view,
    permission_classes,
    authentication_classes,
)
from .models import Review
from .serializer import ReviewSerializer


@api_view(["GET"])
@permission_classes([])
@authentication_classes([])
def get_reviews(request, property_id):
    reviews = Review.objects.filter(property_id=property_id)
    serializer = ReviewSerializer(reviews, many=True)
    return JsonResponse(serializer.data, safe=False)


@api_view(["POST"])
@permission_classes([])
@authentication_classes([])
def create_review(request):
    serializer = ReviewSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, safe=False)
    return JsonResponse(serializer.errors, status=400)
