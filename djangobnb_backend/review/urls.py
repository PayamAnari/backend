from django.urls import path
from . import api


urlpatterns = [
    path("", api.get_reviews, name="api_get_reviews"),
]
