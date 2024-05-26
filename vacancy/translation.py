from modeltranslation.translator import register, TranslationOptions

from vacancy.models import VacancyModel


@register(VacancyModel)
class VacancyModelTranslationOptions(TranslationOptions):
    fields = ('title', 'description')