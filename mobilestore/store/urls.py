from django.urls import path
from .views import *

urlpatterns = [
    path('storehome/',StoreHome.as_view(),name='storehome'),
    path('addpro/',AddProView.as_view(),name='addpro'),
    path('viewpro/',ProductView.as_view(),name='viewpro'),
    path('profile/',ViewProfile.as_view(),name='profile'),
    path('change-password/',PassView.as_view(),name='change-password'),
    path('dltpro/<int:did>',DeleteProd.as_view(),name='dltpro'),
    path('editpro/<int:did>',EditProd.as_view(),name='editpro'),
]
