# Generated by Django 5.1.4 on 2024-12-18 00:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('databank', '0002_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comment',
            field=models.TextField(),
        ),
    ]
