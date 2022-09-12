from tkinter import CURRENT
from django.db import models

# Create your models here.

class Category(models.Model):
    name=models.CharField(max_length=30)
    softDelete=models.IntegerField(default=0)

class Product(models.Model):
    name=models.CharField(max_length=30)
    summary=models.TextField()
    color=models.CharField(max_length=30)
    size=models.CharField(max_length=30)
    price=models.IntegerField()
    softDelete=models.IntegerField(default=0)
    category=models.ForeignKey(Category,on_delete=models.CASCADE,default=1)




# 'Happy Ninja','Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industrys standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged.',
# 'Black,Blue','small,large',18.00,'add to cart'