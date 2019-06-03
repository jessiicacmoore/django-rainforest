from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, reverse
from datetime import date
from django.utils import timezone
from django.contrib.auth.forms import UserCreationForm
from .models import Product


def home_page(request):
    
    context = {'products': Product.objects.all()}
    response = render(request, 'home.html', context)
    return HttpResponse(response)

def root_path(request):
    return HttpResponseRedirect('/home')