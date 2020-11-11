from django.db import models


class Group(models.Model):
    name = models.CharField(max_length=150)
    about = models.TextField(max_length=2048)
    max_student = models.IntegerField(default=15)
    is_evening_group = models.BooleanField(default=True)

    def __str__(self):
        return f'Group - {self.name}'
