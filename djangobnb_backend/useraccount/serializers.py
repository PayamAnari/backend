from rest_framework import serializers

from .models import User


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "name",
            "avatar_url",
            "email",
            "telephone",
            "work",
            "favorite_song",
            "birthday",
            "about_me",
            "address",
            "last_login",
            "date_joined",
        )
