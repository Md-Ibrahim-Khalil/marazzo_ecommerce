from django.urls import path 

from .views import (
    ProductCreateView,
    ProductListView
)

urlpatterns = [
    # localhost:8000/products/create/
    path(
        route="create/",
        view=ProductCreateView.as_view(),
        name="product-create",
    ),
    # localhost:8000/products/list/
    path(
        route="list/",
        view=ProductListView.as_view(),
        name="product-list",
    ),
]

# ProductListView