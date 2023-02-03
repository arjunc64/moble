from django.shortcuts import render,redirect
from django.views.generic import View,CreateView,TemplateView,FormView,UpdateView
from store.models import StoreModel
from .models import Purchase

# Create your views here.

class UserView(View):
    def get(self,request):
        prod=StoreModel.objects.all()
        return render(request,'userhome.html',{'data':prod})
    
class AddtocartView(View):
    def get(self,request):
        prod=StoreModel.objects.all()
        return render(request,'addtocart.html',{'data':prod})
    
# class PurchaseView(TemplateView):
#     def get(request,product_id):
#         item=get_object_or_404(Item, pk=product_id)
#         if request.method=='POST':
#             purchase=Purchase(item=item,customer=request.user,amount=item.price)
#             purchase.save()
#             return redirect('purchase_success')
#         return render(request,'purchase.html',{'item':item})
    
# def purchase_success(request):
#     return render(request,'purchase_success.html')
