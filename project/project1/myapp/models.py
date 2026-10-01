from django.db import models
from django.conf import settings

class Department(models.Model):
    department_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
  
class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)

class Staff(models.Model):
    staff_id = models.AutoField(primary_key=True)
    user = models.OneToOneField(
      settings.AUTH_USER_MODEL,
      on_delete=models.PROTECT        
    )
    staff_number = models.CharField(max_length=20, unique=True)
    full_name = models.CharField(max_length=50)
    department = models.ForeignKey(
      Department,
      on_delete=models.PROTECT
    )