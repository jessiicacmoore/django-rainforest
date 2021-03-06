"""rainforest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', root_path),
    path('home/', home_page, name="home"),
    path('home/<int:id>', product_display, name='product_details'),
    path('home/new', new_product_page, name='new_product'),
    path('home/<int:id>/edit/', edit_product, name='edit_product'),
    path('home/<int:id>/delete', delete_product, name='delete_product'),
    path('home/<int:id>/reviews/create', review_product, name='review_product'),
    path('home/<int:product_id>/reviews/<int:review_id>', edit_review, name='edit_review'),
    path('home/<int:product_id>/reviews/<int:review_id>/delete', delete_review, name='delete_review'),
]
