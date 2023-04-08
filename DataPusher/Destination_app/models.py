from django.db import models
from Account_app.models import User_Account

# Create your models here.
class Destination_model(models.Model):
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=100)
    created_by =  models.ForeignKey(User_Account, on_delete=models.CASCADE)