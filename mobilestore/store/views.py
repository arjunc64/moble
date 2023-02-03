from django.shortcuts import render,redirect
from django.views.generic import View,CreateView,TemplateView,FormView,UpdateView
from .models import StoreModel
from django.urls import reverse_lazy
from .forms import ProductForm
from account.models import User
from django.contrib import messages


# Create your views here.

class StoreHome(TemplateView):
    template_name='addproduct.html'


class AddProView(CreateView):
    template_name='addproduct.html'
    model=StoreModel
    form_class=ProductForm
    success_url=reverse_lazy('editpro')
def post(self,request,*args,**kwargs):
    form_data=self.form_class(request.POST)
    if form_data.is_valid():
        messages.success(request,"Product added!!!")
        return redirect('editpro')
    else:
        messages.success(request,"Product added!!!")
        return redirect(request,"addproduct.html",{'form':form_data})
    
class ProductView(View):
    def get(self,request):
        prod=StoreModel.objects.all()
        return render(request,"editproducts.html",{'data':prod})
    
class DeleteProd(View):
    def get(self,request,*args,**kwargs):
        did=kwargs.get("did")
        item=StoreModel.objects.get(id=did)
        item.delete()
        return redirect('editpro')
    
class EditProd(View):
    def get(self,request,*args,**kwargs):
        d_id=kwargs.get("did")
        item=StoreModel.objects.get(id=d_id)
        form=ProductForm(instance=item)
        return render(request,"editproducts.html",{'form':form})
    def post(self,request,*args,**kwargs):
        d_id=kwargs.get("did")
        item=StoreModel.objects.get(id=d_id)
        form_data=ProductForm(request.POST,files=request.FILES,instance=item)
        if form_data.is_valid():
            form_data.save()
            return redirect('editpro')
        else:
            return redirect('addpro')