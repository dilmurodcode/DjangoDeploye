from django.contrib import admin
from .models import *

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name')
    list_display_links = ('id', 'full_name')


@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    list_display = ('id', 'image')
    list_display_links = ('id', 'image')


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'image')
    list_display_links = ('id', 'image')


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name')
    list_display_links = ('id', 'full_name')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'status')
    list_display_links = ('id', 'status')


@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'image')
    list_display_links = ('id', 'image')


@admin.register(ProductCharacteristic)
class ProductCharacteristicAdmin(admin.ModelAdmin):
    list_display = ('id', 'key')
    list_display_links = ('id', 'key')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('id', 'image')
    list_display_links = ('id', 'image')


@admin.register(CompanyAchievements)
class CompanyAchievementsAdmin(admin.ModelAdmin):
    list_display = ('id', 'year')
    list_display_links = ('id', 'year')


@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')


@admin.register(Achievements)
class AchievementsAdmin(admin.ModelAdmin):
    list_display = ('id', 'image')
    list_display_links = ('id', 'image')


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')








