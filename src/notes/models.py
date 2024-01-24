from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class User(AbstractUser):
    pass


class Note(models.Model):
    text = models.CharField(max_length=300)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
