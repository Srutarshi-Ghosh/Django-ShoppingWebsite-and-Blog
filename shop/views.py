from django.http import HttpResponse
from django.shortcuts import render
from .models import Contact
from  .models import Order
from shop.functions.ShopFunctions import *
import json

def index(request):
    params = set_products_by_category()
    return render(request, 'shop/index.html', params)


def search(request):
    params = search_products(request)
    return render(request, 'shop/search.html', params)


def about(request):
    return render(request, 'shop/about.html')


def contact(request):
    thank = False
    if request.method == "POST":
        set_contacts(request)
        thank = True
    return render(request, 'shop/contact.html', {'thank': thank})


def tracker(request):
    if request.method == "POST":
        return tracker_display(request)

    return render(request, 'shop/tracker.html')



def productView(request, myid):
    product = Product.objects.filter(id=myid)
    return render(request, 'shop/productview.html', {'product': product[0]})


def checkout(request):
    thank = False
    id = ""
    if request.method == "POST":
        order = set_orders(request)
        thank = True
        id = order.order_id
    return render(request, 'shop/checkout.html', {'thank': thank, 'id': id})

