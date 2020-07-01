# Generated by Django 3.0.7 on 2020-06-30 02:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0008_auto_20200629_2007'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='restaurantspage',
            name='restaurant',
        ),
        migrations.AlterField(
            model_name='restaurantpage',
            name='restaurant',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='restaurant.Restaurant'),
        ),
    ]