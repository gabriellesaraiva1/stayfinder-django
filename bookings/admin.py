from django.contrib import admin
from .models import Booking

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ("id", "listing", "guest", "check_in", "check_out", "status", "total_price")
    list_filter = ("status", "check_in")
    search_fields = ("listing__title", "guest__username")
