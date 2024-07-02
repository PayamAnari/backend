from django.http import JsonResponse
from rest_framework.decorators import api_view
from .models import Review
from .serializers import ReviewSerializer


@api_view(["GET"])
def get_reviews(request):
    serializer = ReviewSerializer(Review.objects.all(), many=True)

    return JsonResponse(serializer.data, safe=False)
