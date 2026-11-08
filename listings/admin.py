from django.contrib import admin
from .models import Listing

@admin.register(Listing)
class ListingAdmin(admin.ModelAdmin):
    list_display = ("title", "city", "host", "nightly_price", "active", "created_at")
    list_filter = ("active", "property_type", "city", "wifi", "pool")
    search_fields = ("title", "city", "host__username")
