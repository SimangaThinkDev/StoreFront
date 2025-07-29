from django.shortcuts import render
from store.models import Product

# Create your views here.

def say_hello(request):
    q_set = Product.objects.all()

    for product in q_set:
        print(product)

    return render( request, 'hello.html' )
