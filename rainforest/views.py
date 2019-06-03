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


def product_display(request, id):
    product = Product.objects.get(id=id)
    context = {'product': product}
    return render(request, 'product_detail.html', context)


def root_path(request):
    return HttpResponseRedirect('/home')