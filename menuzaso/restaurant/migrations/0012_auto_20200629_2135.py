# Generated by Django 3.0.7 on 2020-06-30 03:35

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('restaurant', '0011_auto_20200629_2025'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dish',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('currency', models.CharField(choices=[('USD', 'Dolares'), ('NIO', 'Cordobas')], default='NIO', max_length=3)),
            ],
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='staff',
            field=models.ManyToManyField(related_name='restaurants', to=settings.AUTH_USER_MODEL),
        ),
    ]