# Generated by Django 5.0 on 2024-03-25 13:36

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reportapp', '0008_article_status'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='founddate',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='article',
            name='foundlocation',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='article',
            name='lostdate',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='article',
            name='lostlocation',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='article',
            name='user',
            field=models.ForeignKey(max_length=100, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]