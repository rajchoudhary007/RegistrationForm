from django.db import models

# Create your models here.

class Member(models.Model):
     firstname=models.CharField(max_length=30)
     lastname=models.CharField(max_length=30)
     username=models.CharField(max_length=30)
     password=models.CharField(max_length=12)
     address = models.CharField(max_length=100,null=True)
     pincode = models.CharField(max_length=10,null=True)
     course = models.CharField(max_length=100,null=True)
     dob = models.DateField(null=True)
     email = models.EmailField(null=True)
     document = models.FileField(upload_to='documents/',null=True)

     def __str__(self):
        return self.username
    