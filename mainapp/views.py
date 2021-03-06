from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponseNotFound
from .models import Product
from math import ceil
from cart.forms import CartAddProductForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()
    return render(request, 'catalogue.html', {'product': product, 'cart_product_form': cart_product_form})


def categories(request, category):
    products = Product.objects.filter(Category=category)
    pages = ceil(products.count() / 4)
    pages_list = list(range(1, pages + 1))
    return render(request, 'catalogue.html', {'products': products, "pages": pages_list})


def catalogue(request, page=1):
    products_list = Product.objects.all()
    page -= 1
    if page == 0:
        products = products_list[0:4]
    else:
        products = products_list[4 * page:4 * page + 4]
    pages = ceil(products_list.count() / 4)
    pages_list = list(range(1, pages + 1))
    return render(request, 'catalogue.html', {'products': products, "pages": pages_list})


'''
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
'''


def adding(request):
    products = Product.objects.all()
    return render(request, "adding_products.html", {"products": products})


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


def edit_product(request, product_name):
    product = Product.objects.get(Name=product_name)
    if request.method == "POST":
        product.ProductID = request.POST.get('id')
        product.Name = request.POST.get('name')
        product.Description = request.POST.get('description')
        product.Price = request.POST.get('price')
        product.Category = request.POST.get('category')
        product.save()
        return HttpResponseRedirect("/")
    else:
        return render(request, "adding_products.html", {"chosen_product": product})
