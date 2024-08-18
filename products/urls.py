from django.urls import path 

from .views import (
    ProductCreateView,
    ProductListView,
    ProductUpdateView,
    ProductDeleteView
)

urlpatterns = [
    # localhost:8000/products/list/
    path(
        route="list/",
        view=ProductListView.as_view(),
        name="product-list",
    ),
    # localhost:8000/products/create/
    path(
        route="create/",
        view=ProductCreateView.as_view(),
        name="product-create",
    ),
    # localhost:8000/products/update/<int:pk>/
    path(
        route="update/<int:pk>/",
        view=ProductUpdateView.as_view(),
        name="product-update",
    ),
        # localhost:8000/products/delete/<int:pk>/
    path(
        route="delete/<int:pk>/",
        view=ProductDeleteView.as_view(),
        name="product-delete",
    ),
]
