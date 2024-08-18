from rest_framework import serializers
from .models import CustomerProfile

class CustomerProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerProfile
        fields =['user', 'address', 'phone_number']