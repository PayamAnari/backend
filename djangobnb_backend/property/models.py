import uuid
from django.conf import settings
from useraccount.models import User
from django.db import models


class Property(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=225)
    description = models.TextField()
    price_per_night = models.IntegerField()
    bedrooms = models.IntegerField()
    bathrooms = models.IntegerField()
    guests = models.IntegerField()
    country = models.CharField(max_length=225)
    country_code = models.CharField(max_length=10)
    category_code = models.CharField(max_length=10)
    image = models.ImageField(max_length=255)
    address = models.TextField()
    landlord = models.ForeignKey(
        User, related_name="properties", on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


def image_url(self):
    return f"{settings.WEBSITE_URL}{self.image.url}"
