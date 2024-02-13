from rest_framework import serializers
from .models import Build


class BuildSerializer(serializers.ModelSerializer):
    class Meta:
        model = Build
        fields = [
            "id",
            "reference",
            "item",
            "quantity",
            "cost",
            "creation_date",
            "completion_date",
            "status",
        ]
        read_only_fields = [
            "id",
            "creation_date",
        ]
