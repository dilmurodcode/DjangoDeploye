from .models import *
from . import serializers
from rest_framework import views
from rest_framework.response import Response

class CustomerListAPIView(views.APIView):

    def get(self, request):
        queryset = Customer.objects.all()
        serializer = serializers.CustomerSerializer(queryset, many=True)

        return Response(
            data = serializer.data,
            status=200
         )

class PartnerListAPIView(views.APIView):

    def get(self, request):
        queryset = Partner.objects.all()
        serializer = serializers.PartnerSerializer(queryset, many=True)

        return Response(
            data=serializer.data,
            status=200
        )

class NewsListAPIView(views.APIView):

    def get(self, request):
        queryset = News.objects.all()
        serializer = serializers.NewsSerializer(queryset, many=True)

        return Response(
            data=serializer.data,
            status=200
        )

class ApplicationAPIView(views.APIView):

    def get(self, request):
        data = Application.objects.all().values()

        return Response(
            data=data,
            status=200
        )

class ProductAPIView(views.APIView):

    def get(self, request):
        queryset = Product.objects.all()
        serializer = serializers.ProductSerializer(queryset, many=True)

        return Response(
            data=serializer.data,
            status=200
        )

class ProductImageAPIView(views.APIView):

    def get(self, request):
        queryset = ProductImage.objects.all()
        serializer = serializers.ProductImageSerializer(queryset, many=True)

        return Response(
            data=serializer.data,
            status=200
        )

class ProductCharacteristicAPIView(views.APIView):

    def get(self, request):
        queryset = ProductCharacteristic.objects.all()
        serializer = serializers.ProductCharacteristicSerializer(queryset, many=True)

        return Response(
            data=serializer.data,
            status=200
        )

class CategoryAPIView(views.APIView):

    def get(self, request):
        queryset = Category.objects.all()
        serializer = serializers.CategorySerializer(queryset, many=True)

        return Response(
            data=serializer.data,
            status=200
        )

class CompanyAPIView(views.APIView):

    def get(self,request):
        queryset = Company.objects.all()
        serializer = serializers.CompanySerializer(queryset,many=True)

        return Response(
            data=serializer.data,
            status=200
        )

class CompanyAchievementsAPIView(views.APIView):

    def get(self, request):
        queryset = CompanyAchievements.objects.all()
        serializer = serializers.CompanyAchievementsSerializer(queryset, many=True)

        return Response(
            data=serializer.data,
            status=200
        )

class RegionAPIView(views.APIView):

    def get(self, request):
        queryset = Region.objects.all()
        serializer = serializers.RegionSerializer(queryset, many=True)

        return Response(
            data=serializer.data,
            status=200
        )

class AchievementsAPIView(views.APIView):

    def get(self, request):
        queryset = Achievements.objects.all()
        serializer = serializers.AchievementsSerializer(queryset, many=True)

        return Response(
            data=serializer.data,
            status=200
        )

class GalleryAPIView(views.APIView):

    def get(self, request):
        queryset = Gallery.objects.all()
        serializer = serializers.GallerySerializer(queryset, many=True)

        return Response(
            data=serializer.data,
            status=200
        )

