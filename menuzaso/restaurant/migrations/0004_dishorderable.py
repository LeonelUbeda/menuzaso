# Generated by Django 3.0.8 on 2020-07-05 01:50

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0003_dish_managed_by'),
    ]

    operations = [
        migrations.CreateModel(
            name='DishOrderable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('dish', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurant.Dish')),
                ('page', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='restaurant_dish', to='restaurant.RestaurantPage')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
    ]