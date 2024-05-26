from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.filters import OrderingFilter
from rest_framework.response import Response
from rest_framework import viewsets


from product.models import CategoryModel, SubCategoryModel, ProductModel
from product.serializers import CategoryModelSerializer, SubCategoryModelSerializer, ProductModelSerializer, TestCategorySerializer


class CategoryModelListAPIView(ListAPIView):
    ''' Category LIST'''
    queryset = CategoryModel.objects.order_by('my_order')
    serializer_class = CategoryModelSerializer


class SubCategoryModelListAPIView(ListAPIView):
    ''' Subcategory LIST'''
    queryset = SubCategoryModel.objects.order_by('my_order')
    serializer_class = SubCategoryModelSerializer


class CategoryInfoList(APIView):
    def get(self, request, pk):
        cats = CategoryModel.objects.get(id=pk)
        serializer = CategoryModelSerializer(cats, context={'request': request})
        return Response(serializer.data)


class ProductModelListAPIView(ListAPIView):
    ''' Product LIST'''
    queryset = ProductModel.objects.all().order_by('my_order')
    serializer_class = ProductModelSerializer
    ordering_fields = ['my_order']


class CategoryTestViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = CategoryModel.objects.all()
    serializer_class = TestCategorySerializer
