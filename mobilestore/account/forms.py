from django.contrib.auth.forms import UserCreationForm
from .models import User
from django import forms

class UserRegForm(UserCreationForm):
    class Meta:
        model=User
        fields = [
            'first_name','last_name','email','username','password1','password2','phone','address','usertype'
        ]

class LoginForm(forms.Form):
    username=forms.CharField(max_length=120)
    password=forms.CharField(max_length=120,widget=forms.PasswordInput)