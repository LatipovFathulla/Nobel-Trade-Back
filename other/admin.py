from django.contrib import admin

from other.models import HomeVideoModel, PartnersLogoModel, BrandsLogoModel, SubsidiariesLogoModel
from django.utils.translation import gettext_lazy as _
from django.utils.html import format_html


@admin.register(HomeVideoModel)
class HomeVideoModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'video', 'updated_at', 'created_at']
    search_fields = ['id']
    list_filter = ['created_at']


@admin.register(PartnersLogoModel)
class PartnersLogoModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'part_image_tag', 'link', 'updated_at', 'created_at']
    search_fields = ['id']
    list_filter = ['created_at']

    def part_image_tag(self, obj):
        if obj.image:
            return format_html('<img src="{}" height="60" />'.format(obj.image.url))
        else:
            return '-'

    part_image_tag.short_description = _('Image')

@admin.register(SubsidiariesLogoModel)
class SubsidiariesLogoModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'sub_image_tag', 'link', 'updated_at', 'created_at']
    search_fields = ['id']
    list_filter = ['created_at']

    def sub_image_tag(self, obj):
        if obj.image:
            return format_html('<img src="{}" height="60" />'.format(obj.image.url))
        else:
            return '-'

    sub_image_tag.short_description = _('Image')


@admin.register(BrandsLogoModel)
class BrandsLogoModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'brand_image_tag', 'link', 'updated_at', 'created_at']
    search_fields = ['id']
    list_filter = ['created_at']

    def brand_image_tag(self, obj):
        if obj.image:
            return format_html('<img src="{}" height="60" />'.format(obj.image.url))
        else:
            return '-'

    brand_image_tag.short_description = _('Image')