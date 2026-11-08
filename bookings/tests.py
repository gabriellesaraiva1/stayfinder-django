from datetime import date, timedelta
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.test import TestCase
from listings.models import Listing
from .models import Booking

class BookingRulesTests(TestCase):
    def setUp(self):
        self.host = User.objects.create_user(username="host", password="SafePass123!")
        self.guest = User.objects.create_user(username="guest", password="SafePass123!")
        self.listing = Listing.objects.create(
            host=self.host, title="Casa de teste", description="Uma casa confortável",
            city="Maricá", nightly_price="200.00", max_guests=4
        )
    def test_calculates_total_price(self):
        booking = Booking(
            listing=self.listing, guest=self.guest,
            check_in=date(2030, 1, 10), check_out=date(2030, 1, 13), guests=2
        )
        booking.save()
        self.assertEqual(str(booking.total_price), "600.00")
    def test_rejects_overlapping_booking(self):
        Booking.objects.create(
            listing=self.listing, guest=self.guest,
            check_in=date(2030, 1, 10), check_out=date(2030, 1, 13), guests=2
        )
        other = User.objects.create_user(username="guest2", password="SafePass123!")
        with self.assertRaises(ValidationError):
            Booking.objects.create(
                listing=self.listing, guest=other,
                check_in=date(2030, 1, 12), check_out=date(2030, 1, 14), guests=2
            )
