from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, reverse, get_object_or_404
from datetime import date
from django.utils import timezone
from django.contrib.auth.forms import UserCreationForm
from .models import Product
from .forms import ProductForm, ReviewForm


def home_page(request):
    
    context = {'products': Product.objects.all()}
    response = render(request, 'home.html', context)
    return HttpResponse(response)


def product_display(request, id):
    product = Product.objects.get(id=id)
    form = ReviewForm()
    context = {'product': product, 'form': form}
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

def edit_product(request, id):
    obj =  get_object_or_404(Product, pk=id)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect("product_details", id=obj.id)
    else:
        form = ProductForm(instance=obj)
        context = { 'form': form}
        response = render(request, 'product_form.html', context)
    return HttpResponse(response)

def delete_product(request, id):
    obj = get_object_or_404(Product, id=id)
    template_name = 'delete.html'
    if request.method == "POST":
        obj.delete()
        return redirect("home")
    context={"object": obj}
    return render(request, template_name, context)


def review_product(request, id):
    product = get_object_or_404(Product, pk=id)
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.product = product
            review.save()
        return redirect("product_details", id=id)

# def make_delivery(request, id):
#     selected_paperboy = Paperboy.objects.get(id=id)
#     if request.method == "POST":
#         form = DeliveryForm(request.POST)
#         if form.is_valid():
#             start_address = form.cleaned_data.get("starting_house_number")
#             end_address = form.cleaned_data.get("ending_house_number")
#             selected_paperboy.deliver(
#                 start_address=start_address, end_address=end_address
#             )
#             selected_paperboy.save()
#             return redirect("home")
#         else:
#             root()
