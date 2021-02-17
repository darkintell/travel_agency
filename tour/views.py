from django.shortcuts import render
from .models import TourModel, CityModel

# Create your views here.
def home(request):
    context = {}
    context['a'] = 'test'
    context['random_tours'] = TourModel.objects.filter(is_active=True).order_by('?')
    context['top_tours'] = TourModel.objects.filter(is_active=True).order_by('-score')
    context['cities'] = CityModel.objects.order_by('?')
    return render(request, 'index.html',context)