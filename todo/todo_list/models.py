from django.db import models


# Create your models here.
class Task(models.Model):
    description = models.CharField(max_length=64)
    complete = models.BooleanField(default=False)

class Completed(models.Model):
    description = models.CharField(max_length=64)
    task_id = models.IntegerField()
