from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Product, Cafe
from .forms import ProductForm
from django.http import HttpResponseRedirect
from django.template.context_processors import csrf
from django.views.generic.edit import DeleteView
from django.contrib.contenttypes.models import ContentType
from django.urls import reverse

#Serves the index file
def index(request):
    products = Product.objects.all()
    context = {
        'products' : products,
        'cash': Cafe.cash
    }
    return render(request,'index.html',context)

#Add product to database using forms
def addProduct(request):
    if request.method == 'GET':
        form = ProductForm()
    else:
        form = ProductForm(request.POST)
        if form.is_valid():
             name = form.cleaned_data['name']
             price = form.cleaned_data['price']
             obj = Product(productName = name, productPrice = price, numbersSold = 0)
             obj.save()
             return HttpResponseRedirect(('/'))
    return render(request, 'addProduct.html', {'form': form})

#Used for navigating to the html-page for resetting cash
def goToReset(request):
    cafe = get_object_or_404(Cafe, id=Cafe.objects.first().id)
    return render(request, 'reset.html', {'cafe': cafe})
    return HttpResponseRedirect(('/'))

#Resets cash by calling the Cafe-oject's method reset()
def reset(request):
    cafe = get_object_or_404(Cafe, id=Cafe.objects.first().id)
    cafe.reset()
    return HttpResponseRedirect(('/'))

#Buys the product with id equivalent to the attribute of the function,
#calls the product-object's method buy() to handle the counter for the product and the total cash
def kjopProdukt(request, id):
    originalObj = get_object_or_404(Product, id=id)
    originalObj.buy()
    return HttpResponseRedirect(('/'))

#Deletes product with id=id from the database
def productDelete(request, id):
    obj = get_object_or_404(Product, id=id)
    obj.delete()
    return HttpResponseRedirect(('/'))
