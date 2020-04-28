from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    studentName = models.CharField(max_length=30)
    rollNumber = models.IntegerField()
    className = models.CharField(max_length=30)

    def __str__(self):
        return self.studentName