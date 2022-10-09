from django.db import models
from shop.models import *
class cartlist(models.Model):
    class_id = models.CharField(max_length=250,unique=True)
    date_time = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.cart_id
class items(models.Model):
    prod = models.ForeignKey(product,on_delete=models.CASCADE)
    cart = models.ForeignKey(cartlist,on_delete=models.CASCADE)
    quant = models.IntegerField()
    active = models.BooleanField(default=True)
    def __str__(self):
        return self.prod
    def total(self):
        return self.prod.price*self.quant



# Create your models here.
