from django import forms
from .models import Listing

class ListingForm(forms.ModelForm):
    class Meta:
        model = Listing
        exclude = ("host", "active", "created_at")
        widgets = {"description": forms.Textarea(attrs={"rows": 5})}
