from rest_framework.serializers import ModelSerializer

from vacancy.models import VacancyModel


class VacancySerializer(ModelSerializer):
    class Meta:
        model = VacancyModel
        fields = ['id', 'title', 'description', 'image', 'start_time', 'end_time', 'updated_at', 'created_at']