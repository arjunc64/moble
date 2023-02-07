from django.shortcuts import render,redirect
from django.views.generic import View,CreateView,TemplateView,FormView,UpdateView
from django.contrib.auth import authenticate
from .models import StoreModel
from django.urls import reverse_lazy
from .forms import ProductForm,PassForm
from account.models import User
from django.contrib import messages


# Create your views here.

class StoreHome(TemplateView):
    template_name='storehome.html'
def get(self,request):
    prod=StoreModel.objects.all()
    return render(request,'storehome.html',{'data':prod})


class AddProView(CreateView):
    template_name='addproduct.html'
    model=StoreModel
    form_class=ProductForm
    success_url=reverse_lazy('storehome')
def post(self,request,*args,**kwargs):
    form_data=self.form_class(request.POST)
    if form_data.is_valid():
        messages.success(request,"Product added!!!")
        return redirect('storehome')
    else:
        messages.error(request,"Product added!!!")
        return redirect(request,"addproduct.html",{'form':form_data})
    
class ProductView(View):
    def get(self,request):
        prod=StoreModel.objects.all()
        return render(request,"viewproducts.html",{'data':prod})
    
class DeleteProd(View):
    def get(self,request,*args,**kwargs):
        did=kwargs.get("did")
        item=StoreModel.objects.get(id=did)
        item.delete()
        return redirect('viewpro')
    
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
            return redirect('storehome')
        
class ViewProfile(TemplateView):
    template_name="profile.html"
    

class PassView(FormView):
    template_name='password.html'
    form_class=PassForm

    def post(self,request,*args,**kwargs):
        form_data=self.form_class(request.POST)
        if form_data.is_valid():
            old=form_data.cleaned_data.get('old_password')
            new_p=form_data.cleaned_data.get('new_password')
            c_p=form_data.cleaned_data.get('confirm_password')
            user=authenticate(request,username=request.user.username,password=old)
            if user:
                if new_p==c_p:
                    user.set_password(c_p)
                    user.save()
                    messages.success(request,"Password Changed!!")
                    return redirect('log')
                else:
                    messages.error(request,"New Password and confirm password mismatches!!")
                    return redirect('change-password')
            else:
                messages.error(request,"Old Password Mismacthes!!")
                return redirect('change-password')
        else:
            messages.error(request,form_data.errors)
            return redirect('change-password')