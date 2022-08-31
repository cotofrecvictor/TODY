from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.contrib.auth.views import LoginView

from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Sarcini


# Create your views here.

class LogareView(LoginView):
    template_name = 'acasa/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('sarcini')

class ListaSarcini(LoginRequiredMixin, ListView):
    model= Sarcini
    context_object_name = 'sarcini'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sarcini'] = context['sarcini'].filter(utilizator=self.request.user)
        return context

class CreazaSarcina(LoginRequiredMixin, CreateView):
    model = Sarcini
    fields = '__all__'
    success_url = reverse_lazy('sarcini')

class DetaliiSarcina(LoginRequiredMixin, DetailView):
    model = Sarcini
    context_object_name = 'sarcina'
    template_name = 'acasa/sarcina.html'

class EditeazaSarcina(LoginRequiredMixin, UpdateView):
    model = Sarcini
    fields = '__all__'
    success_url = reverse_lazy('sarcini')

class StergeSarcina(LoginRequiredMixin, DeleteView):
    model = Sarcini
    context_object_name = 'sarcini'
    success_url = reverse_lazy('sarcini')
    template_name = 'acasa/sarcina_confirm_delete.html'