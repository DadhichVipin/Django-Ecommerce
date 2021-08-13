from django.urls import path
from . import views

urlpatterns = [
    path('', views.Index.as_view(), name='store'),
    path('cart',views.Cart.as_view(),name='cart'),
]
