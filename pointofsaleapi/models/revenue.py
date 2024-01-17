from django.db import models
from .order import Order

class Revenue(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    total = models.FloatField()
    payment_type = models.CharField(max_length=20)
    tip = models.FloatField()
    order_type = models.CharField(max_length=20)