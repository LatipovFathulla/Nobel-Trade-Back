from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class VacancyConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'vacancy'
    verbose_name = _('Vacancy')