from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=200)
    added_at = models.DateTimeField(auto_now_add=True)


class Tag(models.Model):
    name = models.CharField(max_length=200)
    added_at = models.DateTimeField(auto_now_add=True)


class Item(models.Model):
    sku = models.CharField(max_length=100)
    name = models.CharField(max_length=200)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="items"
    )
    in_stock = models.PositiveIntegerField()
    available_stock = models.PositiveIntegerField()
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    tags = models.ManyToManyField(Tag, related_name="items")
    added_at = models.DateTimeField(auto_now_add=True)
