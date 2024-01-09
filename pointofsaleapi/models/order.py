from django.db import models
from .user import User

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    status = models.CharField(max_length=10)
    customer_phone = models.CharField(max_length=20)
    customer_email = models.CharField(max_length=20)
    type = models.CharField(max_length=10)
    closed = models.BooleanField()
  