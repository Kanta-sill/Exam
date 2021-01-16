from django.db import models

# Create your models here.

class Student(models.Model):

    def __str__(self):
        return self.name

    name=models.CharField(max_length=30)
    username=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    age=models.IntegerField()
    gender=models.CharField(max_length=10)
    email=models.CharField(max_length=50)
    address=models.CharField(max_length=150)
    phone=models.CharField(max_length=15)