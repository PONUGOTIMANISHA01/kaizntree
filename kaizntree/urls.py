from django.contrib import admin
from django.urls import path, include
from .auth_api import UserCreationApiView
from rest_framework.authtoken import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("items/", include("items.urls")),
    path("build/", include("build.urls")),
    # Authentication
    path("login", views.obtain_auth_token, name="login"),
    path("register", UserCreationApiView.as_view(), name="register"),
]
