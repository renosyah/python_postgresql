from django.db import models
import uuid

# Create your models here.
class Student(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nim = models.CharField(max_length=70, blank=False, default='')
    name = models.TextField(blank=False, default='')
    departement = models.CharField(max_length=70, blank=False, default='')
    status = models.IntegerField(blank=False, default=0)