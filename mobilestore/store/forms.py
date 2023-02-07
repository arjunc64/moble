from django import forms
from account.models import User
from .models import StoreModel

class ProductForm(forms.ModelForm):
    class Meta:
        model=StoreModel
        exclude=['store']


class PassForm(forms.Form):
    old_password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    new_password=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    confirm_password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
