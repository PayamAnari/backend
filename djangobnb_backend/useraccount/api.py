from .models import User
from .serializers import UserDetailSerializer
from rest_framework.decorators import (
    api_view,
    authentication_classes,
    permissions_classes,
)
from django.http import JsonResponse


@api_view(["GET"])
@authentication_classes([])
@permissions_classes([])
def landlord_detail(request, pk):
    user = User.objects.get(pk=pk)
    serializer = UserDetailSerializer(user, many=False)

    return JsonResponse(serializer.data, safe=False)
