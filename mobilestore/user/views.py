from django.shortcuts import render,redirect
from django.views.generic import View,CreateView,TemplateView,FormView,UpdateView
from store.models import StoreModel
from .models import Purchase
from django.contrib import messages

# Create your views here.

class UserView(View):
    def get(self,request):
        prod=StoreModel.objects.all()
        return render(request,'userhome.html',{'data':prod})
    
class AddtocartView(View):
    def get(self,request,*args,**kwargs):
        pid=kwargs.get('pid')
        product=product.objects.get(id=pid)
        user=request.user
        MyOrder.objects.create(user=user,product=product,status="cart")
        messages.success(request,"Added to cart")
        return redirect('vcart')
    
class ViewCart(View):
    def get(self,request,*args,**kwargs):
        user=request.user
        cart=MyOrder.objects.filter(user=user,status="cart")
        return render(request,"viewcart.html",{'data':cart})
    
class MyOrder(TemplateView):
    template_name="myorder.html"

class Buynow(TemplateView):
    template_name="Buynow.html"
