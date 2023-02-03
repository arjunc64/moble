from django.db import models

# Create your models here.

class StoreModel(models.Model):
    productpic=models.ImageField(upload_to='products_img',null=True)
    productname=models.CharField(max_length=100)
    productmodel=models.CharField(max_length=100,null=True)
    color=models.CharField(max_length=120,null=True)
    price=models.IntegerField()
    quantity=models.IntegerField(null=True)
    description=models.CharField(max_length=300)