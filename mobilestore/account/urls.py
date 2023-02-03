from django.urls import path
from .views import *

urlpatterns = [
    path('reg/',UserRegView.as_view(),name='reg'),
    path('login/',LoginView.as_view(),name='login')
]
