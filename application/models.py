from django.db import models

class Products(models.Model):
    name=models.CharField(default="",max_length=100)
    address=models.CharField(default="",max_length=200)
    description=models.CharField(default="",max_length=1000)
    image=models.ImageField(null=True,blank=True,upload_to="images/")
    phone=models.CharField(default="",max_length=20)
    def __str__(self):
        return self.name
