from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from dj_rest_auth.jwt_auth import get_refresh_view
from dj_rest_auth.registration.views import RegisterView
from dj_rest_auth.views import LoginView, LogoutView, UserDetailsView
from rest_framework_simplejwt.views import TokenVerifyView
from . import api


urlpatterns = [
    path("register/", RegisterView.as_view(), name="rest_register"),
    path("login/", LoginView.as_view(), name="rest_login"),
    path("logout/", LogoutView.as_view(), name="rest_logout"),
    path("token/refresh/", get_refresh_view().as_view(), name="token_refresh"),
    path("myreservations/", api.reservations_list, name="api_reservations_list"),
    path(
        "<uuid:pk>/reservation/",
        api.property_reservation_detail,
        name="api_property_reservation_detail",
    ),
    path("<uuid:pk>/", api.landlord_detail, name="api_landlord_detail"),
    path("<uuid:pk>/profile/", api.update_landlord, name="api_update_landlord"),
    path("<uuid:pk>/upload-profile/", api.upload_profile, name="upload_profile"),
    path("<uuid:pk>/delete/", api.delete_landlord, name="delete_landlord"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
