from .models import Category
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from .serializers import CategorySerializer
from rest_framework.permissions import IsAdminUser

class CategoryCreateView(CreateAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    
class CategoryUpdateView(UpdateAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    

        
    
class CategoryListView(ListAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    
    #DestroyAPIView

class CategoryDeleteView(DestroyAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
