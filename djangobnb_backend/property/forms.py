from django.forms import ModelForm

from .models import Property, Review


class PropertyForm(ModelForm):
    class Meta:
        model = Property
        fields = (
            "title",
            "description",
            "price_per_night",
            "bedrooms",
            "bathrooms",
            "guests",
            "country",
            "country_code",
            "category",
            "image",
        )


class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = (
            "rating",
            "comment",
        )
