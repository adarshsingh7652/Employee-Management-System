from django.db import models

# Create your models here.
class user(models.Model):
    Name=models.CharField(max_length=50)
    Email=models.CharField(max_length=50)
    Department=models.CharField(max_length=50)
    Position=models.CharField(max_length=50)

