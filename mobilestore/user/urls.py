from django.urls import path
from .views import *

urlpatterns = [
    path('ushome/',UserView.as_view(),name='ushome'),
    path('addtocart/',AddtocartView.as_view(),name='atc')
]