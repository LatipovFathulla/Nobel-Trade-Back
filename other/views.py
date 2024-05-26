from django.shortcuts import render
from rest_framework.generics import ListAPIView

from other.models import HomeVideoModel, PartnersLogoModel, BrandsLogoModel, SubsidiariesLogoModel
from other.serializers import HomeVideoModelSerializer, PartnersLogoModelSerializer, BrandsLogoModelSerializer, \
    SubsidiariesLogoModelSerializer


class HomeVideoModelListAPIView(ListAPIView):
    ''' Videos api '''
    queryset = HomeVideoModel.objects.all()
    serializer_class = HomeVideoModelSerializer


class PartnersLogoModelListAPIView(ListAPIView):
    ''' Logo partners '''
    queryset = PartnersLogoModel.objects.all()
    serializer_class = PartnersLogoModelSerializer


class BrandsLogoModelListAPIView(ListAPIView):
    ''' Logo partners '''
    queryset = BrandsLogoModel.objects.all()
    serializer_class = BrandsLogoModelSerializer


class SubsidiariesLogoModelListAPIView(ListAPIView):
    ''' Logo Subsidiaries (Дочерние компании)'''
    queryset = BrandsLogoModel.objects.all()
    serializer_class = SubsidiariesLogoModelSerializer
