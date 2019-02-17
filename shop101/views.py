from django.shortcuts import render,HttpResponse
from shop101.models import Product
# Create your views here.
def test(request):
    return HttpResponse('HELLO WORLD')

def product(request):
    products = Product.objects.all()
    print(products)
    return render(request,'products_list.html',context={'product_list':products})

def expand(request):
    product = Product.objects.all()
    return render(request,'index2.html')

def expand1(request):
    product = Product.objects.all()
    return render(request,'index3.html')

def expand2(request):
    product = Product.objects.all()
    return render(request,'index4.html')

def expand3(request):
    product = Product.objects.all()
    return render(request,'index5.html')

def show_product(request, id):
    p_id = id
    product = Product.objects.get(id=p_id)
    return render(request, 'show_product.html',context={'product':product})