# Generated by Django 5.0.1 on 2024-02-03 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_productmodel_gmo_en_productmodel_gmo_ru_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='categorymodel',
            name='description_en',
            field=models.TextField(help_text='Описания для вашего категории', null=True, verbose_name='cat_description'),
        ),
        migrations.AddField(
            model_name='categorymodel',
            name='description_ru',
            field=models.TextField(help_text='Описания для вашего категории', null=True, verbose_name='cat_description'),
        ),
        migrations.AddField(
            model_name='categorymodel',
            name='description_uz',
            field=models.TextField(help_text='Описания для вашего категории', null=True, verbose_name='cat_description'),
        ),
        migrations.AddField(
            model_name='categorymodel',
            name='title_en',
            field=models.CharField(help_text='Сюда надо писать названия категории например:РАСТИТЕЛЬНОЕ МАСЛО и т.д', max_length=90, null=True, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='categorymodel',
            name='title_ru',
            field=models.CharField(help_text='Сюда надо писать названия категории например:РАСТИТЕЛЬНОЕ МАСЛО и т.д', max_length=90, null=True, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='categorymodel',
            name='title_uz',
            field=models.CharField(help_text='Сюда надо писать названия категории например:РАСТИТЕЛЬНОЕ МАСЛО и т.д', max_length=90, null=True, verbose_name='title'),
        ),
    ]
