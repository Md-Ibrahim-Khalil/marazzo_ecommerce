from django.urls import path
from .views import (
    CustomerProfileListView,
    CustomerProfileCreateView,
    CustomerProfileUpdateView,
    CustomerProfileDeleteView,
)


urlpatterns = [
    # localhost:8000/CustomerProfile/create/
    path(
        route="create/",
        view=CustomerProfileCreateView.as_view(),
        name="profile-create",
    ),

    # localhost:8000/CustomerProfile/list/
    path(
        route="list/",
        view=CustomerProfileListView.as_view(),
        name="profile-list",
    ),
    # localhost:8000/CustomerProfile/update/<int:pk>/
    path(
        route="update/<int:pk>/",
        view=CustomerProfileUpdateView.as_view(),
        name="profile-update",
    ),
    # localhost:8000/CustomerProfile/delete/<int:pk>/
    path(
        route="delete/",
        view=CustomerProfileDeleteView.as_view(),
        name="profile-delete",
    ),
    
]
