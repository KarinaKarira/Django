from django.db import models
from django.contrib.auth.models import User

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

class Student(models.Model):
    name=models.CharField(max_length=30)
    username=models.CharField(max_length=30)
    sem=models.CharField(max_length=30)

class Committee(models.Model):
    committeeName=models.CharField(max_length=30)
    student=models.ManyToManyField(Student,through='Subscription')

class Subscription(models.Model):
    studentId=models.ForeignKey(Student,on_delete=models.CASCADE)
    committeId=models.ForeignKey(Committee,on_delete=models.CASCADE)
    subscriptionDate=models.DateTimeField(auto_now_add=True)

class Album(models.Model):
    artist=models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    release_date=models.DateField(auto_now=True)
    num_stars=models.IntegerField()



    