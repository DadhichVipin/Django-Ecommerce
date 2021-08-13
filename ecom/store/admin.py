
from django.contrib import admin
from .models.product import Product
from .models.category import Category
from .models.orders import Order



# class for display details in table formate for admin 
class AdminProduct(admin.ModelAdmin):
    list_display = ['name', 'price', 'category']

class ProductCategory(admin.ModelAdmin):
    list_display = ['name']

# Register your models here.
admin.site.register(Product, AdminProduct)
admin.site.register(Category, ProductCategory) 
admin.site.register(Order) 

