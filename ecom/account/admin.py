from account.models import Customer
from django.contrib import admin

# class customer(admin.ModelAdmin):
#     list_display = ['First Name','Last Name', 'Contact', 'Email', 'Password' ]

# Register your models here.
admin.site.register(Customer) 