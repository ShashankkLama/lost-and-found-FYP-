# Generated by Django 5.0 on 2024-03-11 15:44

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reportapp', '0005_article_create_date_alter_article_brand_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='founddate',
            field=models.DateTimeField(default=django.utils.timezone.now, null=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='lostdate',
            field=models.DateTimeField(default=django.utils.timezone.now, null=True),
        ),
    ]