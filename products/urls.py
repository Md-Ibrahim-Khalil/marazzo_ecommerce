from django.urls import path 

from .views import (
    ProductCreateView
)

urlpatterns = [
    # localhost:8000/products/create/
    path(
        route="create/",
        view=ProductCreateView.as_view(),
        name="product-create",
    ),
]