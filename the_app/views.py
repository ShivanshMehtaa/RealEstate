from django.shortcuts import render, redirect
from .models import Listings
from .forms import ListingForm

# Create your views here.
#CRUD -create, retrieve, update, delete, list

def listings_list(request):
    listings = Listings.objects.all()
    context = {
        "listings" : listings
    }
    return render (request, "listings.html", context)


def listings_retrieve(request, pk):
    listing = Listings.objects.get(id = pk)
    context = {
        "listing" :listing
    }
    return render(request , "listing.html", context)


def listings_create(request):
    form = ListingForm()
    if request.method == "POST":
        form = ListingForm(request.POST)
        # print(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
        
    
    context = {
        "form": form
    }
    return render (request, "listing_create.html", context)


def listings_update(request, pk):
    listing = Listings.objects.get(id=pk)
    form = ListingForm(instance=listing)

    if request.method == "POST":
        form = ListingForm(request.POST, instance=listing)
        # print(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
        
    
    context = {
        "form": form
    }
    return render (request, "listings_update.html", context)

def listings_delete(request, pk):
    listing = Listings.objects.get(id=pk)
    listing.delete()
    return redirect("/")
