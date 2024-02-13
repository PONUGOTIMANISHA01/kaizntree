from django.contrib import admin
from .models import Build


@admin.register(Build)
class BuildAdmin(admin.ModelAdmin):

    list_display = [
        "reference",
        "item",
        "quantity",
        "cost",
        "creation_date",
        "completion_date",
        "status",
    ]
