# Generated by Django 4.2.4 on 2023-08-13 09:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0009_remove_orders_item_name_flower_added_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainApp.flower'),
        ),
    ]