from django.urls import path
from .views import *

urlpatterns = [
    path('ushome/',UserView.as_view(),name='ushome'),
    path('addtocart/',AddtocartView.as_view(),name='atc'),
    path('myorder/',MyOrder.as_view(),name='myorder'),
    path('buynow/',MyOrder.as_view(),name='buynow'),
    path('vcart/',ViewCart.as_view(),name='vcart')
]