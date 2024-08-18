from django.shortcuts import render
from .models import Product
from categories.models import Category
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.permissions import IsAdminUser
from .serializers import ProductSerializer
from django.shortcuts import get_object_or_404



class ProductListView(ListAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

class ProductCreateView(CreateAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    