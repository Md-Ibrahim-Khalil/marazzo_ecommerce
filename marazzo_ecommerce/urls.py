from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/admin/login/', TokenObtainPairView.as_view(), name='admin_login'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path("categories/", include("categories.urls")),
    path("products/", include("products.urls")),
    path("CustomerProfile/", include("CustomerProfile.urls")),
    
]


