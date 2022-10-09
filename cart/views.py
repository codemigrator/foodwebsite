from django.shortcuts import render,redirect,get_object_or_404
from shop.models import *
from . models import *
from django.core.exceptions import ObjectDoesNotExist

def cart_details(request,tot=0,count=0,cart_items=None):
    try:
        ct = cartlist.objects.get(class_id=c_id(request))
        ct_items = items.objects.filter(cart=ct,active=True)
        for i in ct_items:
            tot += (i.prod.price*i.quant)
            count += i.quant
    except ObjectDoesNotExist:
        pass
    return render(request,"cart.html",{'ci':ct_items,'t':tot,'cn':count})
def c_id(request):
    ct_id = request.session.session_key
    if not ct_id:
        ct_id = request.session.create()
    return ct_id
def add_cart(request,product_id):
    prodt = product.objects.get(id=product_id)
    try:
        ct = cartlist.objects.get(class_id=c_id(request))
    except cartlist.DoesNotExist:
        ct = cartlist.objects.create(class_id=c_id(request))
        ct.save()
    try:
        c_items = items.objects.get(prod=prodt, cart=ct)
        if c_items.quant < c_items.prod.stock:
            c_items.quant += 1
        c_items.save()
    except items.DoesNotExist:
        c_items = items.objects.create(prod=prodt, quant=1, cart=ct)
        c_items.save()
    return redirect('cartDetails')

def min_cart(request,product_id):
    ct = cartlist.objects.get(class_id=c_id(request))
    pro = get_object_or_404(product, id=product_id)
    c_items = items.objects.get(prod=pro, cart=ct)
    if c_items.quant > 1:
        c_items.quant -= 1
        c_items.save()
    else:
        c_items.delete()
    return redirect('cartDetails')
def cart_delete(request,product_id):
    ct = cartlist.objects.get(class_id=c_id(request))
    pro = get_object_or_404(product, id=product_id)
    c_items = items.objects.get(prod=pro, cart=ct)
    c_items.delete()
    return redirect('cartDetails')


