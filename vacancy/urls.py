from django.urls import path

from vacancy.views import VacancyModelListAPIView

urlpatterns = [
    path('api/v1/vacancies/', VacancyModelListAPIView.as_view(), name='vacancies')
]