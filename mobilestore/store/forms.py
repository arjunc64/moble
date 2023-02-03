from django import forms
from account.models import User
from .models import StoreModel

class ProductForm(forms.ModelForm):
    class Meta:
        model=StoreModel
        fields="__all__"