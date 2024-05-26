from adminsortable2.admin import SortableAdminMixin
from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from modeltranslation.admin import TranslationAdmin
from django.utils.html import format_html

from product.models import CategoryModel, SubCategoryModel, ProductModel


@admin.register(CategoryModel)
class CategoryModelAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ['title', 'created_at', 'my_order']
    search_fields = ['title']
    list_filter = ['created_at']
    ordering = ['my_order']


# SubCategoryModel

@admin.register(SubCategoryModel)
class SubCategoryModelAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ['subcategory', 'created_at', 'my_order']
    search_fields = ['subcategory']
    list_filter = ['created_at']
    ordering = ['my_order']


# Product Model
@admin.register(ProductModel)
class ProductModelAdmin(SortableAdminMixin, TranslationAdmin):
    list_display = ['id', 'title', 'is_new', 'pr_image_tag', 'updated_at', 'created_at', 'my_order']
    search_fields = ['title', 'GMO', 'volume']
    list_filter = ['created_at']
    save_as = True
    save_as_continue = True
    list_max_show_all = True
    save_on_top = True
    ordering = ['my_order']

    def pr_image_tag(self, obj):
        if obj.image:
            return format_html('<img src="{}" height="60" />'.format(obj.image.url))
        else:
            return '-'

    pr_image_tag.short_description = _('Image')
