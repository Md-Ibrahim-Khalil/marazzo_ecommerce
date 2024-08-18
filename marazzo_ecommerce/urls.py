from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("categories/", include("categories.urls")),
    path("products/", include("products.urls")),
    path("CustomerProfile/", include("CustomerProfile.urls")),
]
