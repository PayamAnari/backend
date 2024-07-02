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
