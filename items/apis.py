from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import *
from .serializer import *


# ==================== CATEGORY ===================================
class CategoryListView(APIView):

    permission_classes = [
        permissions.IsAuthenticated,
    ]

    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(instance=categories, many=True)

        return Response(serializer.data)

    def post(self, request):
        serializer = CategorySerializer(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CategoryDetailsView(APIView):
    permission_classes = [
        permissions.IsAuthenticated,
    ]

    def put(self, request, pk):
        category = get_object_or_404(Category, id=pk)
        serializer = CategorySerializer(instance=category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        category = get_object_or_404(Category, id=pk)
        category.delete()
        return Response(status=status.HTTP_200_OK)


# ===================== TAGS ===================================
class TagListView(APIView):

    permission_classes = [
        permissions.IsAuthenticated,
    ]

    def get(self, request):
        categories = Tag.objects.all()
        serializer = TagSerializer(instance=categories, many=True)

        return Response(serializer.data)

    def post(self, request):
        serializer = TagSerializer(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TagDetailsView(APIView):
    permission_classes = [
        permissions.IsAuthenticated,
    ]

    def put(self, request, pk):
        tag = get_object_or_404(Tag, id=pk)
        serializer = TagSerializer(instance=tag, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        tag = get_object_or_404(Tag, id=pk)
        tag.delete()
        return Response(status=status.HTTP_200_OK)


# ===================== ITEMS ===================================


class ItemListView(APIView):

    permission_classes = [
        permissions.IsAuthenticated,
    ]

    def get(self, request):
        query_params = request.GET
        catID = query_params.get("catId", None)
        available = query_params.get("available", None)
        tags = query_params.getlist("tag")

        items = Item.objects.all()

        if catID is not None:
            category = get_object_or_404(Category, id=catID)
            items = items.filter(category=category)

        if available is not None and available == 1:
            items = items.filter(available_stock__gt=1)

        if len(tags) > 0:
            items = items.filter(tags__in=tags)

        serializer = ItemSerializer(instance=items, many=True)

        return Response(serializer.data)

    def post(self, request):
        serializer = ItemSerializer(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ItemDetailsView(APIView):
    permission_classes = [
        permissions.IsAuthenticated,
    ]

    def put(self, request, pk):
        item = get_object_or_404(Item, id=pk)
        serializer = ItemSerializer(instance=item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        item = get_object_or_404(Item, id=pk)
        item.delete()
        return Response(status=status.HTTP_200_OK)
