# Generated by Django 5.1.4 on 2024-12-22 22:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('databank', '0003_alter_comment_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='language',
            name='aa',
            field=models.CharField(blank=True, choices=[(None, '(Unknown)'), ('YES', 'Подтверждённое да'), ('not found', 'Кажется нет'), ('?', 'Непонятно'), ('---', 'Невозможно')], max_length=10),
        ),
        migrations.AlterField(
            model_name='language',
            name='am',
            field=models.CharField(blank=True, choices=[(None, '(Unknown)'), ('YES', 'Подтверждённое да'), ('not found', 'Кажется нет'), ('?', 'Непонятно'), ('---', 'Невозможно')], max_length=10),
        ),
        migrations.AlterField(
            model_name='language',
            name='ma',
            field=models.CharField(blank=True, choices=[(None, '(Unknown)'), ('YES', 'Подтверждённое да'), ('not found', 'Кажется нет'), ('?', 'Непонятно'), ('---', 'Невозможно')], max_length=10),
        ),
        migrations.AlterField(
            model_name='language',
            name='mm',
            field=models.CharField(blank=True, choices=[(None, '(Unknown)'), ('YES', 'Подтверждённое да'), ('not found', 'Кажется нет'), ('?', 'Непонятно'), ('---', 'Невозможно')], max_length=10),
        ),
    ]
