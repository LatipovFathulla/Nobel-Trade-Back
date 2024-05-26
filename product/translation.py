from modeltranslation.translator import register, TranslationOptions
from .models import CategoryModel, SubCategoryModel, ProductModel


@register(CategoryModel)
class CategoryModelTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


@register(SubCategoryModel)
class SubCategoryModelTranslationOptions(TranslationOptions):
    fields = ('subcategory', 'description')


@register(ProductModel)
class ProductModelTranslationOptions(TranslationOptions):
    fields = ('title', 'short_descriptions', 'descriptions')
