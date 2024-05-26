from django.shortcuts import render
from rest_framework.generics import ListAPIView

from vacancy.models import VacancyModel
from vacancy.serializers import VacancySerializer


class VacancyModelListAPIView(ListAPIView):
    ''' Vacancy LIST'''
    queryset = VacancyModel.objects.all()
    serializer_class = VacancySerializer
