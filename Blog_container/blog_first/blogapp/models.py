from django.db import models

# Create your models here.
class Person(models.Model):
    firstName=models.CharField(max_length=30)
    lastName=models.TextField(null=True)

#one person can have many blogs

class Blog(models.Model):
    title=models.CharField(max_length=30)
    content=models.TextField()
    datePosted=models.DateTimeField(null=True) #bydefault null false hota hai mtlb null values nahi dalega 
    personId=models.ForeignKey(Person,on_delete=models.CASCADE,default=1)
    softDelete=models.IntegerField(default=0)

class Pizza(models.Model):
    type=models.CharField(max_length=30)
    pizzaName=models.CharField(max_length=30)

class Topping(models.Model):
    toppingName=models.CharField(max_length=30)
    pizzaTopping=models.ManyToManyField(Pizza)

    