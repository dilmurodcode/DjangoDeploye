from django.urls import path
from . import views

urlpatterns = [
    path('category-list/', views.CustomerListAPIView.as_view()),
    path('partner-list/', views.PartnerListAPIView.as_view()),
    path('news-list/', views.NewsListAPIView.as_view()),
    path('application-list/', views.ApplicationAPIView.as_view()),
    path('product-list/', views.ProductAPIView.as_view()),
    path('product_image-list/', views.ProductImageAPIView.as_view()),
    path('product_characteristic-list/', views.ProductCharacteristicAPIView.as_view()),
    path('category-list/', views.CategoryAPIView.as_view()),
    path('company-list/', views.CompanyAPIView.as_view()),
    path('company_achievements-list/', views.CompanyAchievementsAPIView.as_view()),
    path('region-list/', views.RegionAPIView.as_view()),
    path('achievements-list/', views.AchievementsAPIView.as_view()),
    path('gallery-list/', views.GalleryAPIView.as_view())
]