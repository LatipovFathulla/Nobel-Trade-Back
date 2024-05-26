from django.db import models
from datetime import datetime
import pytz as pytz
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.translation import gettext_lazy as _


class CategoryModel(models.Model):
    title = models.CharField(max_length=90,
                             help_text=_('Сюда надо писать названия категории например:РАСТИТЕЛЬНОЕ МАСЛО и т.д'),
                             verbose_name=_('title'))
    description = models.TextField(help_text=_('Описания для вашего категории'), verbose_name=_('cat_description'))
    my_order = models.PositiveIntegerField(
        default=0,
        blank=False,
        null=False,
        db_index=True,
        verbose_name=_('my_order')
    )
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Updated at'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Created at'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')
        ordering = ['my_order']


class SubCategoryModel(models.Model):
    category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE, related_name=_('subcategory'),
                                 help_text=_('Сюда надо указать категорию'))
    subcategory = models.CharField(max_length=90,
                                   help_text=_(
                                       'Сюда надо писать названия подкатегории например:РАСТИТЕЛЬНОЕ МАСЛО и т.д'),
                                   verbose_name=_('title'))
    description = models.TextField(help_text=_('Описания для вашего подкатегории (Не обьязательно)'),
                                   verbose_name=_('cat_description'), null=True, blank=True)
    my_order = models.PositiveIntegerField(
        default=0,
        blank=False,
        null=False,
        db_index=True,
        verbose_name=_('my_order')
    )
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Updated at'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Created at'))

    def __str__(self):
        return self.subcategory

    class Meta:
        verbose_name = _('Subcategory')
        verbose_name_plural = _('Subcategories')
        ordering = ['my_order']


class ProductModel(models.Model):
    title = models.CharField(max_length=120, verbose_name=_('product_title'),
                             help_text=_('Сюда надо писать название товара например:Кубанское золото..'))
    category = models.ManyToManyField(CategoryModel, related_name='pr_categories',
                                      help_text=_('Тут можете выбрать категории для вашего продукта'), blank=True)
    subcategory = models.ForeignKey(SubCategoryModel, on_delete=models.CASCADE, related_name='pr_subcategories',
                                    help_text=_('Тут можете выбрать подкатегорию для вашего продукта'), null=True,
                                    blank=True)
    short_descriptions = models.TextField(verbose_name=_('product_short_description'),
                                          help_text=_('Сюда надо писать краткое описания для вашего товара'))
    descriptions = RichTextUploadingField(verbose_name=_('product_description'),
                                                 help_text=_('Сюда надо писать описания для вашего товара'))
    # term = models.CharField(max_length=50, verbose_name=_('product_term'),
    #                         help_text=_('Сюда надо писать срок например: 12 месяцев...'))
    # GMO = models.CharField(max_length=30, verbose_name=_('product_GMO'),
    #                        help_text=_('Сюда надо писать с ГМО или БЕЗ ГМО'))
    # substance = models.CharField(max_length=40, verbose_name=_('product_substance'),
    #                              help_text=_('Сюда надо писать вещество например: Без холестерина....'))
    image = models.FileField(upload_to='image', verbose_name=_('product_image'),
                             help_text=_('Сюда надо загрузить изображения товара'))
    objectPDF = models.FileField(upload_to='product_files', verbose_name=_('object_pdf'),
                                 help_text=_('Сюда надо загрузить PDF если необходимо!'), null=True)
    # volume = models.CharField(max_length=50, verbose_name=_('product_volume'),
    #                           help_text=_('Сюда надо указывать обьем в литрах'))
    # count = models.PositiveIntegerField(default=1, verbose_name=_('product_count'),
    #                                     help_text=_('По умолчанию тут стоит 1 если необходимо можете менять'))
    my_order = models.PositiveIntegerField(
        default=0,
        blank=False,
        null=False,
        db_index=True,
        verbose_name=_('my_order')
    )
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Updated at'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Created at'))

    def __str__(self):
        return self.title

    def is_new(self):
        diff = datetime.now(pytz.timezone('Asia/Tashkent')) - self.created_at
        return diff.days <= 3

    class Meta:
        verbose_name = _('Product')
        verbose_name_plural = _('Products')
        ordering = ['my_order']

# class ProductImagesModel(models.Model):
#     product = models.ForeignKey(ProductModel, on_delete=models.CASCADE, related_name='pr_images',
#                                  verbose_name=_('Product_images'))
#     image = models.FileField(upload_to='product_images')
