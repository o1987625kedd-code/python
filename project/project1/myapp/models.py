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
    department = models.ForeignKey(
      Department,
      on_delete=models.PROTECT
    )
class Ticket(models.Model):
  class Status(models.Textchoices):
    PENDING = ("pending","待處理")
    IN_PROGRESS = ("in_progress","處理中")
    CLOSED = ("closed","已結案")
    
  ticket_id = models.Auto_field(primary_key=True)
  student_account = models.ForeignKey(
  settings.AUTH_USER_MODEL,
  on_delete=models.PROTECT,
  related_name="student_tickets"
)
  category = models.ForeignKey(
  Category,
  on_delete=models.PROTECT
)
  title = models.CharField(max_length=100)
  content = models.TextField()
  status = models.CharField(
  max_length=20,
  choices=Status.choices
  )
