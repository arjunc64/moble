from django.shortcuts import render,redirect
from django.views.generic import TemplateView,CreateView,FormView
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.urls import reverse_lazy  
from .models import User
from .forms import UserRegForm,LoginForm
from store.urls import *

# Create your views here.

class Home(TemplateView):
    template_name="home.html"

class UserRegView(CreateView):
    template_name="reg.html"
    model=User
    form_class=UserRegForm
    success_url=reverse_lazy('home')

def post(self,request,*args,**kwargs):
    form_data=self.form_class(request.POST)
    if form_data.is_valid():
        messages.success(request,"Registration Completed!!!")
        return redirect('home')
    else:
        messages.error(request,"Registration Failed")
        return render(request,"reg.html",{'form':form_data})
 
class LoginView(FormView):
    template_name="login.html"
    form_class=LoginForm
    def post(self,request):
        uname=request.POST.get('username')
        psw=request.POST.get('password')
        user=authenticate(request,username=uname,password=psw)
        if user:
            if user.usertype=="store":
                login(request,user)
                return redirect('storehome')
            login(request,user)
            return redirect('ushome')
        else:
            return redirect('login')
        
class SignOut(View):
    def get(self,request,*args,**wargs):
        logout(request)
        return redirect('login')
        
class UserHome(TemplateView):
    template_name="uhome.html"         
