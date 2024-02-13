from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User


class UserCreationApiView(APIView):
    def post(self, request):
        if request.method == "POST":
            data = request.data
            username = data.get("username", None)
            password = data.get("password", None)
            email = data.get("email", "")
            first_name = data.get("first_name", "")
            last_name = data.get("last_name", "")

            if username is None or password is None:
                return Response(
                    {"eror": "username and password are required"},
                    status=status.HTTP_400_BAD_REQUEST,
                )
            try:
                user = User.objects.create_user(
                    username=username,
                    email=email,
                    password=password,
                )
                user.first_name = first_name
                user.last_name = last_name
                user.save()
                return Response(status=status.HTTP_201_CREATED)
            except:
                return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response(status=status.HTTP_400_BAD_REQUEST)
