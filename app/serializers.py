from .models import *
from rest_framework import serializers


class CustomerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Customer
        fields = (
            'id', 'full_name', 'position', 'image', 'description'
        )


class PartnerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Partner
        fields = (
        'id', 'image', 'url', 'order'
        )


class NewsSerializer(serializers.ModelSerializer):

    class Meta:
        model = News
        fields = (
            'id', 'title', 'description', 'image', 'date', 'body'
        )


class ApplicationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Application
        fields = (
            'id', 'full_name', 'phone', 'description', 'product', 'status'
        )

class ProductSerializer(serializers.ModelSerializer):

     class Meta:
         model = Product
         fields = (
             'id', 'title', 'status', 'order', 'image',  'short_description', 'description', 'brand', 'country', 'guarantee', 'is_main_page', 'category'
         )

class ProductImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductImage
        fields = (
            ('id', 'image', 'product')
        )

class ProductCharacteristicSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductCharacteristic
        fields = (
            'id', 'key', 'value', 'order'
        )

class CategorySerializer(serializers.ModelSerializer):
    model = Category
    fields = (
        'id', 'name', 'icon', 'order'
    )

class CompanySerializer(serializers.ModelSerializer):

    class Meta:
        model = Company
        fields = (
            'id', 'title', 'description', 'icon', 'image', 'short_description'
        )

class CompanyAchievementsSerializer(serializers.ModelSerializer):

    class Meta:
        model = CompanyAchievements
        fields = (
            'id', 'year', 'title', 'description', 'image_url'
        )

class RegionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Region
        fields = (
            'id', 'name', 'number'
        )

class AchievementsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Achievements
        fields = (
            'id', 'title', 'image', 'description', 'icon', 'order'
        )

class GallerySerializer(serializers.ModelSerializer):

    class Meta:
        model = Gallery
        fields = (
            'id', 'title', 'url', 'order'
        )