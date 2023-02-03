from django.db import models
from account.models import User
from store.models import StoreModel

# Create your models here.

class Purchase(models.Model):
    item=models.ForeignKey(StoreModel,on_delete=models.CASCADE)
    customer=models.ForeignKey(User,on_delete=models.CASCADE)
    date_of_purchase=models.DateTimeField(auto_now_add=True)
    amount=models.FloatField()