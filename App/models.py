from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Todo(models.Model):
    status_choices = [
        ('Complete', 'Complete'),
        ('Pending', 'Pending')
    ]
    user = models.ForeignKey(
        User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    status = models.CharField(max_length=20, choices=status_choices)

    def __str__(self):
        return self.title
