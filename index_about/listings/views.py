from django.shortcuts import render
from django.http import HttpResponse
from .models import listings


# Create your views here.

def listings_index(request):
    listings_list = listings.objects.all()
    context = {
        'listings_list': listings_list,
    }
    return render(request, 'listings/listings.html',context)
    #return render(request, 'listings/listings.html',{'listings_list': listings_list,})


def listing(request,listing_id):
    listing=listings.objects.get(id=listing_id)
    context = {
        'listing':listing,
    }
    return render(request, 'listings/listing.html', context)


def search(request):
    return render(request, 'listings/search.html')
