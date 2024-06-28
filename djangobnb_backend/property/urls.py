from django.urls import path
from . import api


urlpatterns = [
    path("", api.properties_list, name="api_properties_list"),
    path("create/", api.create_property, name="api_create_property"),
    path("<uuid:pk>/", api.properties_detail, name="api_properties_detail"),
    path("<uuid:pk>/book/", api.book_property, name="api_book_property"),
    path(
        "<uuid:pk>/reservations/",
        api.property_reservations,
        name="api_property_reservations",
    ),
    path("<uuid:pk/reservation/delete/>", api.delete_reservation, name="api_delete_reservation")
    path("<uuid:pk>/payment/", api.payment_intent, name="api_payment_intent"),
    path("<uuid:pk>/toggle_favorite/", api.toggle_favorite, name="api_toggle_favorite"),
    path("<uuid:pk>/editproperty/", api.update_property, name="api_update_property"),
    path("<uuid:pk>/delete", api.delete_property, name="delete_property"),
]
