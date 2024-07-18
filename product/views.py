from django.shortcuts import render
from django.views.generic import ListView
from django.views import View

from . import models

class ListProduct(ListView):
    model = models.Product
    template_name = 'product/list.html'
    context_object_name = 'products'
    paginate_by = 9


class DetailsProduct(View):
    ...
    

class AddToCart(View):
    ...
    

class RemoveToCart(View):
    ...
    

class Finish(View):
    ...
