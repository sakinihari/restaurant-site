from django.shortcuts import render, redirect, get_object_or_404
from cart.models import *
from django.core.exceptions import ObjectDoesNotExist


# Create your views here.
def cart_details(request, tot=0):
    ct_items = None
    try:
        ct = cartlist.objects.get(cart_id=c_id(request))
        ct_items = cart_items.objects.filter(cart=ct, active=True)
        for i in ct_items:
            tot += (i.prodt.price * i.quan)
            # count += i.quan

    except ObjectDoesNotExist:
        pass

    return render(request, "cart.html", {'ci': ct_items, 'to': tot})


def c_id(request):
    ct_id = request.session.session_key
    if not ct_id:
        ct_id = request.session.create()
    return ct_id


def add_cart(request, product_id):
    prod = product.objects.get(id=product_id)
    try:
        ct = cartlist.objects.get(cart_id=c_id(request))
    except cartlist.DoesNotExist:
        ct = cartlist.objects.create(cart_id=c_id(request))
        ct.save()
    try:
        ct_item = cart_items.objects.get(prodt=prod, cart=ct)
        if ct_item.quan < ct_item.prodt.stock:
            ct_item.quan += 1
        ct_item.save()
    except:
        ct_item = cart_items.objects.create(prodt=prod, quan=1, cart=ct)
        ct_item.save()
    return redirect("cartDetails")


def min_cart(request, product_id):
    prod = get_object_or_404(product, id=product_id)
    ct = cartlist.objects.get(cart_id=c_id(request))
    ct_item = cart_items.objects.get(prodt=prod, cart=ct)
    if ct_item.quan > 1:
        ct_item.quan -= 1
        ct_item.save()
    else:
        ct_item.delete()
    return redirect("cartDetails")


def delete_cart(request, product_id):
    prod = get_object_or_404(product, id=product_id)
    ct = cartlist.objects.get(cart_id=c_id(request))
    ct_item = cart_items.objects.get(prodt=prod, cart=ct)
    ct_item.delete()
    return redirect("cartDetails")
