from django.db import models

class Department(models.Model):
    department_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
  
class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)

class Staff(models.Model):
    staff_id = models.AutoField(primary_key=True)