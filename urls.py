from django.urls import path
from . import views

urlpatterns = [
    path('myapp/', views.myapp, name='myapp'),
    path('contact/', views.contact, name='contact'),
    path('product/', views.product, name='product'),
]