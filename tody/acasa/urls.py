from django.urls import path 
from .views import CreazaSarcina, DetaliiSarcina, ListaSarcini,EditeazaSarcina, StergeSarcina, LogareView
from django.contrib.auth.views import LogoutView
urlpatterns = [
    path('login/', LogareView.as_view(), name = 'login'),
    path('logout/', LogoutView.as_view(next_page='login'), name = 'logout'),
    path('', ListaSarcini.as_view(), name = 'sarcini'),
    path('creaza-sarcina/', CreazaSarcina.as_view(), name = 'creaza-sarcina'),
    path('sarcina/<int:pk>/', DetaliiSarcina.as_view(), name = 'sarcina'),
    path('editeaza-sarcina/<int:pk>/', EditeazaSarcina.as_view(), name = 'editeaza-sarcina'),
    path('sterge-sarcina/<int:pk>/', StergeSarcina.as_view(), name = 'sterge-sarcina'),
]