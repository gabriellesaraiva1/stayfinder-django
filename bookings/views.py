from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from listings.models import Listing
from .forms import BookingForm
from .models import Booking

@login_required
def booking_create(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id, active=True)
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.listing = listing
            booking.guest = request.user
            try:
                booking.save()
                messages.success(request, f"Solicitação enviada! Total: R$ {booking.total_price:.2f}")
                return redirect("my_bookings")
            except Exception as exc:
                form.add_error(None, str(exc))
    else:
        form = BookingForm()
    return render(request, "bookings/form.html", {"form": form, "listing": listing})

@login_required
def my_bookings(request):
    bookings = Booking.objects.filter(guest=request.user).select_related("listing")
    return render(request, "bookings/mine.html", {"bookings": bookings})
