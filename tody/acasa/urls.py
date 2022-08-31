from django.urls import path 
from .views import CreazaSarcina, ListaSarcini

urlpatterns = [
    path('', ListaSarcini.as_view(), name = 'sarcini'),
    path('creaza-sarcina/', CreazaSarcina.as_view(), name = 'creaza-sarcina'),
]