from django.urls import path
from . import api


urlpatterns = [
    path("<uuid:property_id>/reviews/", api.get_reviews, name="api_get_reviews"),
]
