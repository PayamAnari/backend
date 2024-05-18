from rest_framework import serializers

from .models import Property


class PropertiesListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = [
            "id",
            "title",
            "description",
            "price_per_night",
            "bedrooms",
            "bathrooms",
            "guests",
            "country",
            "country_code",
            "category_code",
            "image",
            "address",
            "landlord",
            "created_at",
            "updated_at",
        ]
