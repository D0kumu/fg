# Generated by Django 4.2.4 on 2023-08-11 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0005_alter_flower_category_alter_flower_color_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flower',
            name='category',
            field=models.CharField(default=None, max_length=200),
        ),
        migrations.AlterField(
            model_name='flower',
            name='color',
            field=models.CharField(default=None, max_length=200),
        ),
        migrations.AlterField(
            model_name='flower',
            name='name',
            field=models.CharField(default=None, max_length=200),
        ),
        migrations.AlterField(
            model_name='flower',
            name='scientific_name',
            field=models.CharField(default=None, max_length=200),
        ),
    ]