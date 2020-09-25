from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.shortcuts import render
from django.http import HttpResponse
from .models import listings


# Create your views here.

def listings_index(request):
    listings_ = listings.objects.all()

    paginator=Paginator(listings_,1)
    page = request.GET.get('page',1)
    #paged_listings=paginator.get_page(page)
    try:
        listings_=paginator.page(page)
    except PageNotAnInteger:
        listings_=paginator.page(1)
    except EmptyPage:
        listings_=paginator.page(paginator.num_pages)

    context = {
        #'listings_list': listings_list,
        'listings_list':listings_,
    }
    return render(request, 'listings/listings.html',context)
    #return render(request, 'listings/listings.html',{'listings_list': listings_list,})


def listing(request,listing_id):
    listing1=listings.objects.get(id=listing_id)
    context = {
        'listing1':listing1,
    }
    return render(request, 'listings/listing.html', context)


def search(request):
    return render(request, 'listings/search.html')
