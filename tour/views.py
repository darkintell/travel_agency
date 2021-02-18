from django.shortcuts import render, get_object_or_404
from .models import TourModel, CityModel

# Create your views here.
def home(request):
    context = {
    'a' : 'test',
    'random_tours' : TourModel.objects.filter(is_active=True).order_by('?'),
    'top_tours' : TourModel.objects.filter(is_active=True).order_by('-score'),
    'cities' : CityModel.objects.order_by('?'),
    }
    return render(request, 'index.html',context)


def tour_detail(request, slug):
    context = {
    'tour' : get_object_or_404(TourModel, slug=slug),
    'tours' : TourModel.objects.filter(is_active=True).order_by('-score'),
    }
    return render(request, 'tour-detail.html',context)

def city_detail(request, slug):
    context = {
    'city' : get_object_or_404(CityModel, slug=slug),
    'tours' : TourModel.objects.filter(is_active=True).order_by('-score'),
    }
    return render(request, 'city-detail.html',context)

def tour_listing(request):
    context={
        'tours': TourModel.objects.filter(is_active=True).order_by('-date_created'),
    }
    return render(request, 'tour-listing.html',context)
    
def city_lising(request):
    context = {
        'cities' : CityModel.objects.all()[:5],
        'tours': TourModel.objects.filter(is_active=True).order_by('-date_created'),
    }
    return render(request, 'city-listing.html', context)