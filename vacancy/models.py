from django.db import models
from django.utils.translation import gettext_lazy as _


class VacancyModel(models.Model):
    title = models.CharField(max_length=90, verbose_name=_('vacancy_title'),
                             help_text=_('Тут должны писать название вакансии например:Финансист...'))
    description = models.TextField(verbose_name=_('vacancy_description'),
                                   help_text=_('Тут должны писать описание(характеристики) вашего вакансии'))
    image = models.FileField(upload_to='vacancy_images')
    start_time = models.CharField(max_length=30, verbose_name=_('Начало работы'), help_text=_('Начало работы например 9:00'), default='09:00')
    end_time = models.CharField(max_length=30, verbose_name=_('Окончание работы'), help_text=_('Окончание работы например 18:00'), default='19:00')
    # price = models.FloatField(verbose_name=_('vacancy_price'), help_text=_('Тут указываете ЗП'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Updated at'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Created at'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Vacancy')
        verbose_name_plural = _('Vacancy')
