from rest_framework.views import APIView
from rest_framework import permissions, status
from rest_framework.response import Response

from items.models import Item
from .models import Build
from django.shortcuts import get_object_or_404
from .serializers import BuildSerializer


class BuildListView(APIView):
    permission_classes = [
        permissions.IsAuthenticated,
    ]

    def get(self, request):
        query_params = request.GET
        itemId = query_params.get("itemId", None)
        status = query_params.get("status", None)

        builds = Build.objects.all()

        if itemId is not None:
            item = get_object_or_404(Item, id=itemId)
            builds = builds.where(item=item)

        if status is not None:
            builds = builds.where(status=status)

        serializer = BuildSerializer(instance=builds, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = BuildSerializer(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BuildDetailsView(APIView):
    permission_classes = [
        permissions.IsAuthenticated,
    ]

    def get(self, request, pk):
        build = get_object_or_404(Build, id=pk)
        serializer = BuildSerializer(instance=build)
        return Response(serializer.data)

    def put(self, request, pk):
        build = get_object_or_404(Build, id=pk)
        serializer = BuildSerializer(instance=build, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        build = get_object_or_404(Build, id=pk)
        build.delete()
        return Response(status=status.HTTP_200_OK)
