from django.urls import path

from products.views import index
from products.views import products

app_name = 'products'

urlpatterns = [
     path('', products, name='index')

]

