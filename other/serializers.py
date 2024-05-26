from rest_framework.serializers import ModelSerializer

from other.models import HomeVideoModel, PartnersLogoModel, BrandsLogoModel, SubsidiariesLogoModel


class HomeVideoModelSerializer(ModelSerializer):
    class Meta:
        model = HomeVideoModel
        fields = ['id', 'video', 'updated_at', 'created_at']


class PartnersLogoModelSerializer(ModelSerializer):
    class Meta:
        model = PartnersLogoModel
        fields = ['id', 'image', 'link', 'updated_at', 'created_at']


class BrandsLogoModelSerializer(ModelSerializer):
    class Meta:
        model = BrandsLogoModel
        fields = ['id', 'image', 'link', 'updated_at', 'created_at']


class SubsidiariesLogoModelSerializer(ModelSerializer):
    class Meta:
        model = SubsidiariesLogoModel
        fields = ['id', 'image', 'link', 'updated_at', 'created_at']
