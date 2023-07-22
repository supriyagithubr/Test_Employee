from django.db import models

# Create your models here.

class Employee(models.Model):
    e_id = models.IntegerField()
    e_name = models.CharField(max_length=90)
    salary = models.FloatField()
    city = models.CharField(max_length=80)
    c_name = models.CharField(max_length=70)