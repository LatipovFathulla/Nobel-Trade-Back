# Generated by Django 4.2.9 on 2024-02-13 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('other', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PartnersLogoModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(help_text='Сюда загружайте логотип для партрера и одну', upload_to='partners_logos', verbose_name='partners_logo')),
                ('link', models.TextField(blank=True, help_text='Сюда вы должны поставить ссылку на сайт партнера или т.д НО НЕ Обязательно!', null=True, verbose_name='partners_link')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
            ],
            options={
                'verbose_name': 'Partners_logo',
                'verbose_name_plural': 'Partners_logos',
            },
        ),
        migrations.CreateModel(
            name='SubsidiariesLogoModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(help_text='Сюда загружайте логотип дочерних компаний и одну', upload_to='subsidiaries_logos', verbose_name='subsidiaries_logo')),
                ('link', models.TextField(blank=True, help_text='Сюда вы должны поставить ссылку на сайт дочернего компании или т.д НО НЕ Обязательно!', null=True, verbose_name='subsidiaries_link')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
            ],
            options={
                'verbose_name': 'Subsidiaries_logo',
                'verbose_name_plural': 'Subsidiaries_logos',
            },
        ),
    ]
