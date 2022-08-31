from django.urls import path 
from .views import CreazaSarcina, DetaliiSarcina, ListaSarcini,EditeazaSarcina

urlpatterns = [
    path('', ListaSarcini.as_view(), name = 'sarcini'),
    path('creaza-sarcina/', CreazaSarcina.as_view(), name = 'creaza-sarcina'),
    path('sarcina/<int:pk>/', DetaliiSarcina.as_view(), name = 'sarcina'),
    path('editeaza-sarcina/<int:pk>/', EditeazaSarcina.as_view(), name = 'editeaza-sarcina'),
]