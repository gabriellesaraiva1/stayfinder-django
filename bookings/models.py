from django.conf import settings
from django.core.exceptions import ValidationError
from django.db import models
from django.db.models import Q
from listings.models import Listing

class Booking(models.Model):
    class Status(models.TextChoices):
        PENDING = "PENDING", "Pendente"
        CONFIRMED = "CONFIRMED", "Confirmada"
        CANCELLED = "CANCELLED", "Cancelada"

    listing = models.ForeignKey(Listing, on_delete=models.PROTECT, related_name="bookings")
    guest = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="bookings")
    check_in = models.DateField()
    check_out = models.DateField()
    guests = models.PositiveSmallIntegerField(default=1)
    status = models.CharField(max_length=12, choices=Status.choices, default=Status.PENDING)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def clean(self):
        errors = {}
        if self.check_out <= self.check_in:
            errors["check_out"] = "A saída precisa ser depois da entrada."
        if self.guests < 1 or self.guests > self.listing.max_guests:
            errors["guests"] = f"Esta hospedagem aceita até {self.listing.max_guests} hóspedes."
        if self.guest_id and self.listing_id and self.guest_id == self.listing.host_id:
            errors["guest"] = "O anfitrião não pode reservar o próprio imóvel."
        if self.check_in and self.check_out and self.listing_id:
            overlap = Booking.objects.filter(
                listing_id=self.listing_id,
                status__in=[self.Status.PENDING, self.Status.CONFIRMED],
                check_in__lt=self.check_out,
                check_out__gt=self.check_in,
            )
            if self.pk:
                overlap = overlap.exclude(pk=self.pk)
            if overlap.exists():
                errors["check_in"] = "Já existe uma reserva para parte desse período."
        if errors:
            raise ValidationError(errors)

    def save(self, *args, **kwargs):
        if self.listing_id and self.check_in and self.check_out and self.check_out > self.check_in:
            self.total_price = self.listing.nightly_price * (self.check_out - self.check_in).days
        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Reserva #{self.pk} - {self.listing.title}"
