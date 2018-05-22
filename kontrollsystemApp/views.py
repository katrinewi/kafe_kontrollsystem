from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Product
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
        'products' : products

    }
    return render(request,'index.html',context)

#Add product to database
def addProduct(request):
    if request.method == 'GET':
        form = ProductForm()
    else:
        form = ProductForm(request.POST)
        if form.is_valid():
             Produktnavn = form.cleaned_data['Produktnavn']
             Pris = form.cleaned_data['Pris']
             obj = Product(productName = Produktnavn, productPrice = Pris, numbersSold = 0)
             obj.save()
             return HttpResponseRedirect(('/'))
    return render(request, 'addProduct.html', {'form': form})

def success(request):
    return HttpResponse('Produktet ble lagt til!')

#Delete-knapp
def productDelete(request, id):
    print(request)
    obj = get_object_or_404(Product, id=id)
    #if request.method == "POST":
    obj.delete()
    return HttpResponseRedirect(('/'))
    #context = {
#        "object" : obj
#    }
#    return render(request, "index.html", context)

#def kjopProdukt(request, id):
#    obj = get_object_or_404(Product, id=id)
#    if request.method == "POST":
#        obj.numbersSold +=1
        #pengerIKassa++
#        return HttpResponseRedirect(reverse('index'))
#    context = {
#        "object" : obj
#        "pengerIKassa" : #???
#    }
#    return render(request, "", context)
