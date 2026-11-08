from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render
from .forms import ListingForm
from .models import Listing

def home(request):
    listings = Listing.objects.filter(active=True)
    destination = request.GET.get("destino", "").strip()
    guests = request.GET.get("hospedes", "").strip()
    max_price = request.GET.get("preco", "").strip()
    if destination:
        listings = listings.filter(Q(city__icontains=destination) | Q(state__icontains=destination) | Q(title__icontains=destination))
    if guests.isdigit():
        listings = listings.filter(max_guests__gte=int(guests))
    if max_price:
        try:
            listings = listings.filter(nightly_price__lte=max_price.replace(",", "."))
        except Exception:
            pass
    return render(request, "listings/home.html", {"listings": listings, "destination": destination})

def listing_detail(request, pk):
    listing = get_object_or_404(Listing, pk=pk, active=True)
    return render(request, "listings/detail.html", {"listing": listing})

@login_required
def listing_create(request):
    if request.method == "POST":
        form = ListingForm(request.POST)
        if form.is_valid():
            listing = form.save(commit=False)
            listing.host = request.user
            listing.save()
            messages.success(request, "Sua hospedagem foi publicada!")
            return redirect("listing_detail", pk=listing.pk)
    else:
        form = ListingForm()
    return render(request, "listings/form.html", {"form": form, "heading": "Anuncie sua hospedagem"})

@login_required
def listing_edit(request, pk):
    listing = get_object_or_404(Listing, pk=pk, host=request.user)
    if request.method == "POST":
        form = ListingForm(request.POST, instance=listing)
        if form.is_valid():
            form.save()
            messages.success(request, "Anúncio atualizado.")
            return redirect("listing_detail", pk=listing.pk)
    else:
        form = ListingForm(instance=listing)
    return render(request, "listings/form.html", {"form": form, "heading": "Editar hospedagem"})
