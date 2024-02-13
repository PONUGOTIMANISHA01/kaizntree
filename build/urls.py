from django.urls import path
from .apis import *


urlpatterns = [
    path("", BuildListView.as_view(), name="build_list"),
    path("<int:pk>", BuildDetailsView.as_view(), name="build_details"),
]
