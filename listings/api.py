from rest_framework import viewsets, permissions
from .models import Listing
from .serializers import ListingSerializer

class ListingViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = ListingSerializer
    permission_classes = [permissions.AllowAny]
    queryset = Listing.objects.filter(active=True).select_related("host")
    search_fields = ["title", "city", "state", "description"]
    filterset_fields = ["property_type", "city", "wifi", "pool", "parking"]
