from django.urls import path
from .views import home, tour_detail, city_detail, tour_listing, city_lising, about_us
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', home, name='home'),
    path('tours/<slug:slug>',tour_detail, name='tour-detail'),
    path('city/<slug:slug>', city_detail, name='city-detail'),
    path('CityListing', city_lising, name='city-listing'),
    path('TourListing', tour_listing, name='tour-listing'),
    path('aboutus',about_us, name='about-us'),
] + static(settings.STATIC_URL, document_root= settings.STATIC_ROOT)