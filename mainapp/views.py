from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Product
from math import ceil

# Create your views here.


def adding(request):
    return render(request, "adding_products.html")


def add_product(request):
    if request.method == 'POST':
        product = Product()
        product.ProductID = request.POST.get('id')
        product.Name = request.POST.get('name')
        product.Description = request.POST.get('description')
        product.Price = request.POST.get('price')
        product.Category = request.POST.get('category')
        product.save()
    return HttpResponseRedirect("/")


def delete_product(request):
    product_to_delete = Product.objects.filter(ProductID=request.POST.get('delete_product'))
    product_to_delete.delete()
    return HttpResponseRedirect("/")


def catalogue(request):
    products = Product.objects.all()
    number_of_pages = ceil(Product.objects.count() / 4)
    list_of_pages = []
    for i in range(number_of_pages):
        list_of_pages.append(i)
    return render(request, "catalogue.html", {'products': products, 'pages': list_of_pages})
