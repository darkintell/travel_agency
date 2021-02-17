from django.urls import path
from .views import home, tour_detail, city_detail
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', home, name='home'),
    path('tours/<slug:slug>',tour_detail, name='tour-detail'),
    path('city/<slug:slug>', city_detail, name='city-detail'),
] + static(settings.STATIC_URL, document_root= settings.STATIC_ROOT)