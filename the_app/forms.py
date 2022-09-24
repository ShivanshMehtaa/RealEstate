from turtle import title
from django.forms import ModelForm, Form

from .models import Listings

class ListingForm(ModelForm):
    class Meta:
        model = Listings
        fields = [
            "title", 
            "price",
            "num_bedrooms",
            "num_bathrooms",
            "square_ft",
            "address",
        ]