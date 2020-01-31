from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Product
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def catalogue(request):
    list_of_products = Product.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(list_of_products, 4)

    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)
    return render(request, 'catalogue.html', {'products': products})


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

'''''''''
def catalogue(request):
    products = Product.objects.all()
    return render(request, "catalogue.html", {'products': products})
'''''
