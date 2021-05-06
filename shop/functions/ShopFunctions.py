from django.http import HttpResponse
import json
from shop.models import *
from math import ceil

def set_products_by_category():
    allProducts = []
    catprods = Product.objects.values('category', 'id')
    categories = {item['category'] for item in catprods}
    for cat in categories:
        prod = Product.objects.filter(category=cat)
        no_of_slides = ceil(len(prod) / 4)
        allProducts.append([prod, range(1, no_of_slides), no_of_slides])

    params = {'allProducts': allProducts}
    return params


def search_products(request):
    query = request.GET.get('search')
    allProducts = []
    catprods = Product.objects.values('category', 'id')
    categories = {item['category'] for item in catprods}
    for cat in categories:
        prod_temp = Product.objects.filter(category=cat)
        prod = [item for item in prod_temp if search_match(query, item)]
        no_of_slides = ceil(len(prod) / 4)

        if len(prod) > 0:
            allProducts.append([prod, range(1, no_of_slides), no_of_slides])

    params = {'allProducts': allProducts, 'msg': ""}
    if len(allProducts) == 0 or len(query) < 3:
        params = {'msg': 'Please make sure to enter relevant search query'}
    return params

def set_orders(request):
    items_json = request.POST.get('itemsJson', '')
    name = request.POST.get('name', '')
    amount = request.POST.get('amount', '')
    email = request.POST.get('email', '')
    phone = request.POST.get('phone', '')
    address = request.POST.get('address', '')
    city = request.POST.get('city', '')
    state = request.POST.get('state', '')
    zip_code = request.POST.get('zip_code', '')
    order = Order(items_json=items_json, name=name, amount=amount, email=email, phone=phone, address=address, city=city, state=state, zip_code=zip_code)
    order.save()

    update = OrderUpdate(order_id=order.order_id, update_desc="Your Order has been Placed")
    update.save()

    return order


def set_contacts(request):
    name = request.POST.get('name', '')
    email = request.POST.get('email', '')
    phone = request.POST.get('phone', '')
    desc = request.POST.get('desc', '')
    contact = Contact(name=name, email=email, phone=phone, desc=desc)
    contact.save()


def tracker_display(request):
    order_id = request.POST.get('orderId', '')
    email = request.POST.get('email', '')
    try:
        order = Order.objects.filter(order_id=order_id, email=email)
        if len(order):
            update = OrderUpdate.objects.filter(order_id=order_id)
            updates = []
            for item in update:
                updates.append({'text': item.update_desc, 'time': item.timestamp})
            response = json.dumps({"status": "success", "updates": updates, "itemsJson": order[0].items_json}, default=str)
            return HttpResponse(response)
        else:
            return HttpResponse('{"status": "no item"}')
    except Exception as e:
        return HttpResponse('{"status": "error"}')


def search_match(query, item):
    query = query.lower()
    if query in item.desc.lower() or query in item.category.lower() or query in item.product_name.lower():
        return True
    return False