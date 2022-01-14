import time
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponseRedirect
from django.core.urlresolvers import reverse
import datetime


# Create your views here.
from carts.models import Cart, CartItem

from products.models import Stock

from .models import Order
from .utils import id_generator
from django.contrib.auth import get_user_model


def orders(request):

    #### Parse the old commands 
    print request.session.keys()
    print '-------------'

    user_id = request.session['_auth_user_id']

    User = get_user_model()
    user = User.objects.get(id=user_id)
    orders_id = Order.objects.filter(user =user )
    print orders_id

    items = []
    for ord in orders_id:
        products = CartItem.objects.filter(cart = ord.cart)
        items = items + [[ord, products]]
        print [ord, products]
        print products
        print "========="

    print items
    context = {'items': items}
    template = 'orders/user.html'
    return render(request, template, context)

def order_status(request):

    user_id = request.session['_auth_user_id']
    User = get_user_model()
    user = User.objects.get(id=user_id)
    orders_id = Order.objects.filter(user =user )
    for ord in orders_id:
        print ord.timestamp.strftime('%Y-%m-%d')
    print '-----'

    numdays=10
    base = datetime.datetime.today()
    date_list = [base - datetime.timedelta(days=x) for x in range(numdays)]

    aux = []
    for a in date_list:
        nr = Order.objects.filter(timestamp__month=a.month, 
                      timestamp__day=a.day)
                      ## status='Finished'
        print a, "--", nr
        aux = aux + [[a.strftime('%Y-%m-%d'), len(nr)]]

    print date_list
    print aux


    # Test data for chart
    a = [[orders_id[0].timestamp.strftime('%Y-%m-%d'),1], [orders_id[1].timestamp.strftime('%Y-%m-%d'),1],
        [orders_id[2].timestamp.strftime('%Y-%m-%d'), 2]]
    print a
    context = {'data':a, 'orders': aux}
    template = 'orders/orders_status.html'
    return render(request, template, context)    

# require user login
@login_required
def checkout(request):
    
    try:
        the_id = request.session['cart_id']
        cart = Cart.objects.get(id=the_id)
    except :
        the_id = None
        return HttpResponseRedirect(reverse('cart'))
        
    try:
        new_order = Order.objects.get(cart=cart)
    except Order.DoesNotExist:
        new_order = Order(cart=cart)
        new_order.user = request.user
        new_order.order_id = id_generator()
        new_order.save()
    except:
        # work on some error message
        return HttpResponseRedirect(reverse('cart'))



    # run credit cart
    if new_order.status == "Finished":
        del request.session['cart_id']
        del request.session['items_total']
        return HttpResponseRedirect(reverse('cart'))


    context = {}
    #template = 'products/home.html'


    cart_items = CartItem.objects.filter(cart=cart)

    # print cart_items
    # print len(cart_items)
    context = {'cartItems': cart_items, 'cart':cart}
    template = 'orders/submit.html'
    return render(request, template, context)


# Finish the order 
def complete_order(request):
    q = request.GET.get('addr1')
    print "---"
    print q
    print "---"


    try:
        the_id = request.session['cart_id']
        cart = Cart.objects.get(id=the_id)
    except :
        the_id = None
        return HttpResponseRedirect(reverse('cart'))
        
    try:
        new_order = Order.objects.get(cart=cart)
    except Order.DoesNotExist:
        new_order = Order(cart=cart)
        new_order.user = request.user
        new_order.order_id = id_generator()
        new_order.save()
    except:
        # work on some error message
        return HttpResponseRedirect(reverse('cart'))


    new_order.status = 'Finished'
    new_order.save()

    ## Update the stock
    ## * Quantity
    stock = Stock.objects.all()
    st = stock[0]

    products = CartItem.objects.filter(cart = new_order.cart)
    for p in products:
        print p.product.lapte
        print p.quantity
        st.faina -= p.product.faina * p.quantity
        st.oua -= p.product.oua * p.quantity
        st.lapte -= p.product.lapte * p.quantity
        st.ciocolata -= p.product.ciocolata * p.quantity
        st.frisca -= p.product.frisca * p.quantity
        st.save()

    



    # run credit cart
    if new_order.status == "Finished":
        del request.session['cart_id']
        del request.session['items_total']
        context = {'order' : new_order}
        template = 'orders/order_completed.html'
        return render(request, template, context)  


    context = {}
    #template = 'products/home.html'

    template = 'orders/user.html'
    return render(request, template, context)    