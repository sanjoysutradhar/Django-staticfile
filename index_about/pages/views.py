from django.shortcuts import render
from django.http import HttpResponse
from listings.models import listings
from realtors.models import Realtor


# Create your views here.

def index(request):
    latest = listings.objects.order_by('-list_date')[:3]
    # select= from listings ordered by list_date desc
    return render(request, 'pages/index.html', {'latest_list': latest})


def about(request):
    team=Realtor.objects.order_by('-contact_date')[:3]
    context={
        'team':team
    }
    return render(request, 'pages/about.html',context)
