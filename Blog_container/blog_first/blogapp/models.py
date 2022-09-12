from django.db import models
from django.contrib.auth.models import User

# Create your models here.
#one person can have many blogs

class Blog(models.Model):
    title=models.CharField(max_length=30)
    content=models.TextField()
    datePosted=models.DateTimeField(null=True) #bydefault null false hota hai mtlb null values nahi dalega 
    personId=models.ForeignKey(User,on_delete=models.CASCADE,default=1)
    softDelete=models.IntegerField(default=0)




    