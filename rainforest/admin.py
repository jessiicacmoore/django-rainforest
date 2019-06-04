from django.contrib.admin import site
from rainforest.models import Product, Review

site.register(Product)
site.register(Review)
