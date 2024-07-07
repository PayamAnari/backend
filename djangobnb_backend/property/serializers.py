from rest_framework import serializers
from .models import Property, Reservation
from useraccount.serializers import UserDetailSerializer


class PropertiesListSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(read_only=True)
    landlord = UserDetailSerializer(read_only=True, many=False)
    city = serializers.CharField(max_length=255)

    class Meta:
        model = Property
        fields = (
            "id",
            "title",
            "price_per_night",
            "image_url",
            "landlord",
            "created_at",
            "country",
            "city",
        )


class PropertiesDetailSerializer(serializers.ModelSerializer):
    landlord = UserDetailSerializer(read_only=True, many=False)
    city = serializers.CharField(max_length=255)
    bed = serializers.IntegerField()

    class Meta:
        model = Property
        fields = (
            "id",
            "title",
            "description",
            "price_per_night",
            "image_url",
            "bedrooms",
            "bathrooms",
            "bed",
            "guests",
            "landlord",
            "country",
            "city",
            "category",
        )


class ReservationListSerializer(serializers.ModelSerializer):
    property = PropertiesListSerializer(read_only=True, many=False)
    price_per_night = serializers.FloatField(
        source="property.price_per_night", read_only=True
    )

    class Meta:
        model = Reservation
        fields = (
            "id",
            "start_date",
            "end_date",
            "number_of_nights",
            "total_price",
            "property",
            "price_per_night",
            "status",
        )
