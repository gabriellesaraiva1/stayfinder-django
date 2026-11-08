from django.conf import settings
from django.db import models

class Listing(models.Model):
    class PropertyType(models.TextChoices):
        APARTMENT = "APARTMENT", "Apartamento"
        HOUSE = "HOUSE", "Casa"
        CABIN = "CABIN", "Cabana"
        OTHER = "OTHER", "Outro"

    host = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="listings")
    title = models.CharField(max_length=140)
    description = models.TextField()
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100, blank=True)
    address = models.CharField(max_length=255, blank=True)
    property_type = models.CharField(max_length=20, choices=PropertyType.choices, default=PropertyType.APARTMENT)
    nightly_price = models.DecimalField(max_digits=10, decimal_places=2)
    max_guests = models.PositiveSmallIntegerField(default=2)
    bedrooms = models.PositiveSmallIntegerField(default=1)
    bathrooms = models.PositiveSmallIntegerField(default=1)
    image = models.URLField(blank=True, help_text="URL de uma imagem pública (MVP).")
    wifi = models.BooleanField(default=False)
    pool = models.BooleanField(default=False)
    parking = models.BooleanField(default=False)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.title
