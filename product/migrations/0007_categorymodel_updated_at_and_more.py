# Generated by Django 5.0.1 on 2024-02-03 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_productmodel_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='categorymodel',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Updated at'),
        ),
        migrations.AlterField(
            model_name='categorymodel',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Created at'),
        ),
    ]
