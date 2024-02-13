from rest_framework import serializers
from .models import *


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = [
            "id",
            "name",
            "added_at",
        ]
        read_only_fields = [
            "id",
            "added_at",
        ]


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        read_only_fields = [
            "id",
            "added_at",
        ]
        fields = [
            "id",
            "name",
            "added_at",
        ]


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = [
            "id",
            "sku",
            "name",
            "cost",
            "category",
            "in_stock",
            "available_stock",
            "tags",
        ]

        read_only_fields = [
            "id",
        ]

    # def create(self, validated_data):
    #     tags = validated_data.pop('tags')
    #     category = validated_data.pop('category')
    #     album = Item.objects.create(**validated_data)
    #     for track_data in tracks_data:
    #         Track.objects.create(album=album, **track_data)
    #     return album
