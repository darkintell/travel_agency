from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import TourModel, CityModel

# Create your views here.
def home(request):
    context = {
    'top' : CityModel.objects.all()[:2],
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
    tours_page = TourModel.objects.filter(is_active=True).order_by('-date_created')
    
    search_name = request.GET.get('city')
    search_date = request.GET.get('date')
    search_price = request.GET.get('price')
    
    if search_name:
        tours_page = tours_page.filter(city__name=search_name)
    if search_date:
        tours_page = tours_page.filter(start_date=search_date)
    if search_price:
        tours_page = tours_page.filter(adult_price__lt=search_price)
    paginator = Paginator(tours_page, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context={
        'tours': page_obj,
    }
    return render(request, 'tour-listing.html',context)
    
def city_lising(request):
    # Pagination
    cities = CityModel.objects.all()
    paginator = Paginator(cities, 8)
    page_num = request.GET.get('page')
    page_obj = paginator.get_page(page_num)
    context = {
        'cities' : page_obj,
        'tours': TourModel.objects.filter(is_active=True).order_by('-date_created'),
    }
    return render(request, 'city-listing.html', context)