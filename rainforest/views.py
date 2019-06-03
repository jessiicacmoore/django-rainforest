from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, reverse
from datetime import date
from django.utils import timezone
from django.contrib.auth.forms import UserCreationForm
from .models import Product
from .forms import ProductForm


def home_page(request):
    
    context = {'products': Product.objects.all()}
    response = render(request, 'home.html', context)
    return HttpResponse(response)


def product_display(request, id):
    product = Product.objects.get(id=id)
    context = {'product': product}
    return render(request, 'product_detail.html', context)


def new_product_page(request):

    # Create Product
    if request.method == "POST":
        form = ProductForm(request.POST)

        if form.is_valid():
            instance = form.save()
            return redirect('product_details', id=instance.id)
        else:
            return render(request, 'product_form.html', {'form':form})
    else:
        form = ProductForm()
        return render(request, 'product_form.html', {'form':form})

def root_path(request):
    return HttpResponseRedirect('/home')