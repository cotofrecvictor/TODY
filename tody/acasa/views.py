from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Sarcini

# Create your views here.

class ListaSarcini(ListView):
    model= Sarcini
    context_object_name = 'sarcini'