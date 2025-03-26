from .models import *
from . import serializers
from rest_framework import views
from rest_framework.response import Response

class CategoryListAPIView(views.APIView):

    def get(self, request):
        queryset = Category.objects.filter().first()
        serializer = serializers.CategorySerializer(queryset, many=False)

        return Response(
            data = serializer.data,
            status=200
         )


class CustomersListAPIView(views.APIView):

    def get(self, request):
        queryset = Customers.objects.all()
        serializer = serializers.CustomersSeralizer(queryset, many=True)

        return Response(
            data = serializer.data,
            status=200
         )