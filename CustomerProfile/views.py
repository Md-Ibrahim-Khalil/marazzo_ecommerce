from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .models import CustomerProfile
from .serializers import CustomerProfileSerializer
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView


class CustomerProfileListView(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CustomerProfileSerializer
    queryset = CustomerProfile.objects.all()
    
    
class CustomerProfileCreateView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CustomerProfileSerializer
    queryset = CustomerProfile.objects.all()
    
class CustomerProfileUpdateView(UpdateAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = CustomerProfileSerializer
    queryset = CustomerProfile.objects.all()

class CustomerProfileDeleteView(DestroyAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = CustomerProfileSerializer
    queryset = CustomerProfile.objects.all()  
  

    
