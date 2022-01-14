from django.shortcuts import render, Http404

# Create your views here.

from .models import Product, ProductImage , Stock

## Search For a product
def search(request):
    try:
        q = request.GET.get('q')
    except:
        q = None

    if q:
        products = Product.objects.filter(title__icontains=q)
        context = {'query': q, 'products': products}
        template = 'products/results.html'
    else:
        template = 'products/home.html'
        context = {}

    return render(request, template, context)


## Home Page 
def stock(request):
    faina_total = 201
    oua_total = 200
    lapte_total = 30
    ciocolata_total = 10
    frisca_total = 10

    stock = Stock.objects.all()
    st = stock[0]

    faina_p = (100 * st.faina) / faina_total
    oua_p = (100 * st.oua) / oua_total
    lapte_p = (100 * st.lapte) / lapte_total
    ciocolata_p = (100 * st.ciocolata) / ciocolata_total
    frisca_p = (100 * st.frisca) / frisca_total

    template = 'products/stock.html'
    context = {'stock': stock[0],
             "faina": faina_p,
             "oua" : oua_p,
             "lapte": lapte_p,
             "ciocolata": ciocolata_p,
             "frisca": frisca_p}
    
    return render(request, template, context)



## Home Page 
def home(request):
    products = Product.objects.all()
    template = 'products/home.html'
    context = {'products': products}
    
    return render(request, template, context)


def torturi(request):
    products = Product.objects.filter(product_type=1)
    template = 'products/torturi.html'
    context = {'products': products}
    
    return render(request, template, context)


def prajituri(request):
    products = Product.objects.filter(product_type=2)
    template = 'products/prajituri.html'
    context = {'products': products}
    
    return render(request, template, context)


## All products
def all(request):

    products = Product.objects.all()
    context = {'products': products}
    template = 'products/all.html'
    return render(request, template, context)



## reverse('single_product', ... )

def single(request, slug):
    try:
        product = Product.objects.get(slug=slug)
        #images = product.productimage_set.all()

        images = ProductImage.objects.filter(product=product)
        context = {'product': product, 'images': images}
        template = 'products/single.html'
        return render(request, template, context)    
    except:
        raise Http404