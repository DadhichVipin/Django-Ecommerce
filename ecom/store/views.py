from typing import List
from store.models.category import Category
from store.models.product import Product
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models.product import Product
from .models.category import Category
from django.views import View


# Create your views here.
class Index(View):

    def post(self, request):
        Product = request.POST.get('product') # product is value of name atribute of input tag in index.html
        remove = request.POST.get('remove')
        cart = request.session.get('cart')
        if cart:
            quantity = cart.get(Product)
            if quantity:
                if remove:
                    if quantity <= 1:
                        cart.pop(Product)
                    else:
                        cart[Product] = quantity - 1

                else:
                    cart[Product] = quantity + 1
            else:
                cart[Product] = 1
        else:
            cart = {}
            cart[Product] = 1

        request.session['cart'] = cart
        print('cart : ',request.session['cart'])
        return redirect('store')
        


    def get(self, request):
        
        cart = request.session.get('cart')
        if not cart:
            request.session['cart'] = {}

        products = None
        categories = Category.get_all_categories()

        
        categoryID = request.GET.get('category',None)
        if categoryID:
            products = Product.get_all_products_by_categoryid(categoryID)
        else:
            products = Product.get_all_products()
        
        data = {}
        data['products'] = products
        data['categories'] = categories
        print(' you are ',request.session.get('email')) # to check in terminal
        return render(request, "index.html", data)


    
class Cart(View):
    def get(self, request):
        ids = list(request.session.get('cart').keys())
        products = Product.get_products_by_id(ids) 
        print(products)
        return render(request, 'cart.html', {'products' : products})

