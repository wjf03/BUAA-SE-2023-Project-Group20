from django.db import models

# Create your models here.

class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=50)
    sex = models.CharField(max_length=20)
    ifManager = models.BooleanField()