from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.views.generic.detail import DetailView
from django.contrib.auth.views import LoginView

from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

from .models import Sarcini


# Create your views here.

class LogareView(LoginView):
    template_name = 'acasa/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('sarcini')

class PaginaInregistrare(FormView):
    template_name = 'acasa/inregistrare.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('sarcini')

    def form_valid(self,form):
        utilizator = form.save()
        if utilizator is not None:
            login(self.request, utilizator)
        return super(PaginaInregistrare, self).form_valid(form)

class ListaSarcini(LoginRequiredMixin, ListView):
    model= Sarcini
    context_object_name = 'sarcini'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sarcini'] = context['sarcini'].filter(utilizator=self.request.user)
        return context

class CreazaSarcina(LoginRequiredMixin, CreateView):
    model = Sarcini
    fields = ['titlu','completat']
    success_url = reverse_lazy('sarcini')

    def form_valid(self, form):
        form.instance.utilizator = self.request.user
        return super(CreazaSarcina, self).form_valid(form)

class DetaliiSarcina(LoginRequiredMixin, DetailView):
    model = Sarcini
    context_object_name = 'sarcina'
    template_name = 'acasa/sarcina.html'

class EditeazaSarcina(LoginRequiredMixin, UpdateView):
    model = Sarcini
    fields = ['titlu','completat']
    success_url = reverse_lazy('sarcini')

class StergeSarcina(LoginRequiredMixin, DeleteView):
    model = Sarcini
    context_object_name = 'sarcini'
    success_url = reverse_lazy('sarcini')
    template_name = 'acasa/sarcina_confirm_delete.html'