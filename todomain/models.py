from django.db import models

# Create your models here.
class TodoItem(models.Model):
    check = models.BooleanField(default=False)
    content = models.CharField(max_length=50)
