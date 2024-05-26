from django.urls import path

from other.views import HomeVideoModelListAPIView, PartnersLogoModelListAPIView, BrandsLogoModelListAPIView,\
                    SubsidiariesLogoModelListAPIView

urlpatterns = [
     path('api/v1/catalog-video/', HomeVideoModelListAPIView.as_view()),
     path('api/v1/partners/', PartnersLogoModelListAPIView.as_view()),
     path('api/v1/brands/', BrandsLogoModelListAPIView.as_view()),
     path('api/v1/subsidiaries/', SubsidiariesLogoModelListAPIView.as_view())
]