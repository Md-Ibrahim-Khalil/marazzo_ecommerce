from django.urls import path
from .views import (
    CategoryCreateView,
    CategoryListView,
    CategoryUpdateView,
    CategoryDeleteView
)


urlpatterns = [
    # localhost:8000/categories/create/
    path(
        route="create/",
        view=CategoryCreateView.as_view(),
        name="category-create",
    ),
    # localhost:8000/categories/update/<int:pk>/
    path(
        route="update/<int:pk>/",
        view=CategoryUpdateView.as_view(),
        name="category-update",
    ),
    # localhost:8000/categories/list/
    path(
        route="list/",
        view=CategoryListView.as_view(),
        name="category-list",
    ),
    # localhost:8000/categories/delete/<int:pk>/
    path(
        route="delete/<int:pk>/",
        view=CategoryDeleteView.as_view(),
        name="category-delete",
    ),
    
]
