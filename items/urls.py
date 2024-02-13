from django.urls import path
from .apis import *


urlpatterns = [
    # Tags
    path("tags", TagListView.as_view(), name="tag_list"),
    path("tags/<int:pk>", TagDetailsView.as_view(), name="tag_details"),
    # Tags
    path("categories", CategoryListView.as_view(), name="category_list"),
    path("categories/<int:pk>", CategoryDetailsView.as_view(), name="category_details"),
    # Items
    path("", ItemListView.as_view(), name="item_list"),
    path("<int:pk>", ItemDetailsView.as_view(), name="item_details"),
]
