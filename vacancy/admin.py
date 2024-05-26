from django.contrib import admin
from django.utils.html import format_html
from modeltranslation.admin import TranslationAdmin
from django.utils.translation import gettext_lazy as _

from vacancy.models import VacancyModel


@admin.register(VacancyModel)
class VacancyModelAdmin(TranslationAdmin):
    list_display = ['id', 'title', 'vac_image_tag', 'updated_at', 'created_at']
    search_fields = ['title']
    list_filter = ['created_at']
    save_as = True
    save_as_continue = True
    list_max_show_all = True
    save_on_top = True

    def vac_image_tag(self, obj):
        if obj.image:
            return format_html('<img src="{}" height="60" />'.format(obj.image.url))
        else:
            return '-'

    vac_image_tag.short_description = _('Image')
