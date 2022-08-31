from django.urls import path 
from .views import ListaSarcini

urlpatterns = [
    path('', ListaSarcini.as_view(), name = 'sarcini'),
]