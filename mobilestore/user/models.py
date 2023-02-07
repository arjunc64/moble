from django.db import models
from account.models import User
from store.models import StoreModel

# Create your models here.

class Purchase(models.Model):
    product=models.ForeignKey(StoreModel,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    date=models.DateTimeField(auto_now_add=True)
    qty=models.IntegerField(default=1)
    status=models.CharField(max_length=100,null=True)