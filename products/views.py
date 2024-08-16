from django.shortcuts import render
from .models import Product
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAdminUser
from .serializers import ProductSerializer

class ProductCreateView(CreateAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = ProductSerializer
    queryset = Product.objects.all()