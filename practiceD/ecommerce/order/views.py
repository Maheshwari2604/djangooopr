# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from order.models import Order
from cart.models import Cart 
import time
from django.shortcuts import render, HttpResponse, HttpResponseRedirect, reverse

# Create your views here.
def Orders(request):
        order = Order.objects.all()
        context = {"order":order}
        template = "orders/user.html"
        return render(request, template, context)

def checkout(request):
    
    try:
        the_id = request.session['cart_Id']
        cart = Cart.objects.get(id=the_id)
        #print cart
    
    except:
        the_id = None
        return HttpResponseRedirect(reverse("view"))

    neworder, created = Order.objects.get_or_create(cart=cart)

    if created:
        neworder.Order_id = str(time.time())
        neworder.save()

    if neworder.status == "Finished":
        #abc.delete()     
        del request.session['cart_Id']
        del request.session['item_total']
        message = "Your Order is placed, you will get information soon"
        context = {"message":message}
        template = 'products/home.html'
        return render(request, template, context)

    message = "Your Order is ready to placed, you will get information soon"
    context = {"message":message}
    template = 'products/home.html'
    return render(request, template, context)