from django.db import models

# Create your models here.
class staff(models.Model):
    name=models.CharField(max_length=100)
    designation=models.CharField(max_length=100)
    department=models.CharField(max_length=100)
    salary=models.IntegerField()
    experience=models.IntegerField()

