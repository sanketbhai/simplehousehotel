


from django.urls import path
from .views import *
urlpatterns = [
   
    path('',index,name='index'),
    path('cart/',cart,name='cart'),
    path('placeorder/',placeorder,name='placeorder'),
    path('about/',about,name='about'),
    path('contact/',contact,name='contact'),


]
