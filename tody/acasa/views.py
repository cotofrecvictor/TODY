from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
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

class DetaliiSarcina(DetailView):
    model = Sarcini
    context_object_name = 'sarcina'
    template_name = 'acasa/sarcina.html'

class EditeazaSarcina(UpdateView):
    model = Sarcini
    fields = '__all__'
    success_url = reverse_lazy('sarcini')

class StergeSarcina(DeleteView):
    model = Sarcini
    context_object_name = 'sarcini'
    success_url = reverse_lazy('sarcini')
    template_name = 'acasa/sarcina_confirm_delete.html'