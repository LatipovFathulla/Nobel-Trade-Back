from django.db import models
from django.utils.translation import gettext_lazy as _


class HomeVideoModel(models.Model):
    video = models.FileField(upload_to='home_videos', verbose_name=_('home_videos'), help_text=_('Сюда загружайте видео для главного страницы и одну'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Updated at'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Created at'))

    def __str__(self):
        return str(self.pk)

    class Meta:
        verbose_name = _('Home video')
        verbose_name_plural = _('Home videos')


class PartnersLogoModel(models.Model):
    image = models.FileField(upload_to='partners_logos', verbose_name=_('partners_logo'), help_text=_('Сюда загружайте логотип для партрера и одну'))
    link = models.TextField(verbose_name=_('partners_link'), help_text=_('Сюда вы должны поставить ссылку на сайт партнера или т.д НО НЕ Обязательно!'), null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Updated at'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Created at'))

    def __str__(self):
        return str(self.pk)

    class Meta:
        verbose_name = _('Partners_logo')
        verbose_name_plural = _('Partners_logos')


class BrandsLogoModel(models.Model):
    image = models.FileField(upload_to='brands_logos', verbose_name=_('brands_logo'), help_text=_('Сюда загружайте логотип для бренда и одну'))
    link = models.TextField(verbose_name=_('brands_link'), help_text=_('Сюда вы должны поставить ссылку на сайт бренда или т.д НО НЕ Обязательно!'), null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Updated at'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Created at'))

    def __str__(self):
        return str(self.pk)

    class Meta:
        verbose_name = _('Brand_logo')
        verbose_name_plural = _('Brands_logos')


class SubsidiariesLogoModel(models.Model):
    image = models.FileField(upload_to='subsidiaries_logos', verbose_name=_('subsidiaries_logo'), help_text=_('Сюда загружайте логотип дочерних компаний и одну'))
    link = models.TextField(verbose_name=_('subsidiaries_link'), help_text=_('Сюда вы должны поставить ссылку на сайт дочернего компании или т.д НО НЕ Обязательно!'), null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Updated at'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Created at'))

    def __str__(self):
        return str(self.pk)

    class Meta:
        verbose_name = _('Subsidiaries_logo')
        verbose_name_plural = _('Subsidiaries_logos')
