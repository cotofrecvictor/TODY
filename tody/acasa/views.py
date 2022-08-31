from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .models import Sarcini


# Create your views here.

class ListaSarcini(ListView):
    model= Sarcini
    context_object_name = 'sarcini'

class CreazaSarcina(CreateView):
    model = Sarcini
    fields = '__all__'
    success_url = reverse_lazy('sarcini')