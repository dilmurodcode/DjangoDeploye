from .models import *
from rest_framework import serializers


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = (
            'id', 'name', 'icon', 'order'
        )

class CustomersSeralizer(serializers.ModelSerializer):

    class Meta:
        model = Customers
        fields = (
            'id', 'full_name', 'image', 'url', 'order'
        )