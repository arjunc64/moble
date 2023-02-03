from django.urls import path
from .views import *

urlpatterns = [
    path('storehome/',StoreHome.as_view(),name='storehome'),
    path('addpro/',AddProView.as_view(),name='addpro'),
    path('viewpro/',ProductView.as_view(),name='viewpro'),
    path('editpro/',ProductView.as_view(),name='editpro'),
]
