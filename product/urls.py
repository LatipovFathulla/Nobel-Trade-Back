from django.urls import path, include
from rest_framework.routers import DefaultRouter

from product.views import CategoryModelListAPIView, SubCategoryModelListAPIView, \
            ProductModelListAPIView, CategoryInfoList, CategoryTestViewSet

router = DefaultRouter()
router.register(r'test-categories', CategoryTestViewSet)

urlpatterns = [
    path('api/v1/categories/', CategoryModelListAPIView.as_view()),
    path('api/v1/subcategories/', SubCategoryModelListAPIView.as_view()),
    path('api/v1/products/', ProductModelListAPIView.as_view()),
    path('api/v1/category/<int:pk>', CategoryInfoList.as_view()),
    path('', include(router.urls)),
    # path('api/v1/category-test/', CategoryTestViewSet.as_view()),
]