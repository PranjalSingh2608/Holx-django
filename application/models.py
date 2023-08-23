from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User


class Products(models.Model):
    user=models.ForeignKey(User,null=
                           True,on_delete=models.SET_NULL)
    name=models.CharField(default="",max_length=100)
    address=models.CharField(default="",max_length=200)
    description=models.CharField(default="",max_length=1000)
    image=models.CharField("images",null=True,blank=True,max_length=1000)
    phone=models.CharField(default="",max_length=20)
    def __str__(self):
        return self.name
