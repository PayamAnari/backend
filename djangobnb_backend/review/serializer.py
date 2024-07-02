from rest_framework import serializers
from .models import Review
from useraccount.serializers import UserDetailSerializer
from property.serializers import PropertiesDetailSerializer


class ReviewSerializer(serializers.ModelSerializer):
    user = UserDetailSerializer(read_only=True)
    property = PropertiesDetailSerializer(read_only=True)

    class Meta:
        model = Review
        fields = [
            "id",
            "property",
            "user",
            "rating",
            "comment",
            "created_at",
            "updated_at",
        ]
