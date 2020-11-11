from django.db import models
from groups.models import Group


class Student(models.Model):
    name = models.CharField(max_length=64)
    age = models.IntegerField()
    gender = models.CharField(max_length=64, null=True, blank=True)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}'
