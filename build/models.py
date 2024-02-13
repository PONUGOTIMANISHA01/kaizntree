from django.db import models
from items.models import Item


class Build(models.Model):
    STATUS_CHOICES = [
        ("CMP", "Completed"),
        ("PND", "pending"),
        ("CNL", "Canceled"),
    ]
    reference = models.CharField(max_length=200)
    item = models.ForeignKey(
        Item, on_delete=models.SET_NULL, null=True, related_name="builds"
    )
    quantity = models.PositiveIntegerField()
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    creation_date = models.DateTimeField(auto_now_add=True)
    completion_date = models.DateTimeField(null=True)
    status = models.CharField(max_length=3, choices=STATUS_CHOICES, default="PND")
