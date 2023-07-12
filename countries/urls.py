from django.urls import path
from countries.views import get_countries, get_country, post_country


urlpatterns = [
    path('', get_countries, name='list-country'),
    path('create/', post_country, name='create-country'),
    path('detail/<int:id>/', get_country, name='get-country')
]
