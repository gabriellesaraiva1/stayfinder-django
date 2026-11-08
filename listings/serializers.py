from rest_framework import serializers
from .models import Listing

class ListingSerializer(serializers.ModelSerializer):
    host_name = serializers.CharField(source="host.get_full_name", read_only=True)
    class Meta:
        model = Listing
        fields = ["id", "host_name", "title", "description", "city", "state", "property_type",
                  "nightly_price", "max_guests", "bedrooms", "bathrooms", "image",
                  "wifi", "pool", "parking", "created_at"]
        read_only_fields = ["id", "host_name", "created_at"]
