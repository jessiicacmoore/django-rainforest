from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, reverse, get_object_or_404
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

# @login_required
# def edit_post(request, id):
#     post = get_object_or_404(Article, pk=id, user=request.user.pk)
#     if request.method == "POST":
#         form = ArticleForm(request.POST, instance=post)
#         if form.is_valid():
#             updated_post = form.save()
#             return HttpResponseRedirect(reverse('post_details', args=[post.id]))
#     else:
#         form = ArticleForm(instance=post)
#     context = {'title': 'Edit Post', 'form': form, 'post': post}
#     html_response = render(request, "edit_post.html", context)
#     # return HttpResponse(html_response)


# def blog_edit_view(request, id):
#     obj = get_object_or_404(Article, id = id)
#     if request.method == "POST":
#         form = ArticleForm(request.POST, instance= obj)
#         if form.is_valid():
#             obj = form.save(commit=False)
#             obj.published_date = timezone.now()
#             obj.save()
#             # template_name = 'post_edit.html'
#             # context = {"title": f"Updated {obj.title} at {obj.published_date}", "form": form}
#             # return render(request, template_name, context)
#             return redirect('blog_details', id=obj.id)
#     else:
#         form = ArticleForm(instance=obj)
#         current_date = date.today()
#     return render(request, 'update.html', {'form':form, 'date': current_date  })
