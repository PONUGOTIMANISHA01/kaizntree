from django.contrib import admin
from .models import Tag, Category, Item


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "added_at",
    ]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "added_at",
    ]


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    def item_tags(self, obj):
        return ", ".join([i.name for i in obj.tags.all()])

    list_display = [
        "name",
        "added_at",
        "sku",
        "name",
        "category",
        "in_stock",
        "available_stock",
        "cost",
        "item_tags",
        "added_at",
    ]
