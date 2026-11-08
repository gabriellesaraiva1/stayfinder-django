from django.urls import path
from . import views
urlpatterns = [
    path("nova/<int:listing_id>/", views.booking_create, name="booking_create"),
    path("minhas/", views.my_bookings, name="my_bookings"),
]
