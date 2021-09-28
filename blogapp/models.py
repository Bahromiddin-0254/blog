from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class CustomUser(User):
    class Meta:
        proxy = True

class Person(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(null=True)
    def __str__(self):
        return self.name