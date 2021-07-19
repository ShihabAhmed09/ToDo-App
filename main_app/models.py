from django.db import models
from django.utils import timezone


class Task(models.Model):
    name = models.CharField(max_length=200)
    start_time = models.DateTimeField(default=timezone.now)
    end_time = models.DateTimeField(null=True, blank=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.name
