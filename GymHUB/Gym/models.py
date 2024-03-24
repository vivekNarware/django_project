from django.db import models

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=50)
    age=models.CharField(max_length=10)
    gender=models.CharField(max_length=70)
    locality=models.CharField(max_length=150)
    email=models.CharField(max_length=50)
    number=models.CharField(max_length=20)
    
