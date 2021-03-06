# Generated by Django 3.0.8 on 2020-07-03 08:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields
import streams.blocks
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0045_assign_unlock_grouppagepermission'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60, null=True)),
                ('slug', models.SlugField()),
                ('staff', models.ManyToManyField(related_name='restaurants', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='RestaurantPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('content', wagtail.core.fields.StreamField([('category_block', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(help_text='Nombre de la categoria', required=True)), ('background', wagtail.images.blocks.ImageChooserBlock(help_text='Imagen de fondo de categoria', required=True)), ('dishes', wagtail.core.blocks.ListBlock(streams.blocks.DishesStructBlock))])), ('logo_block', wagtail.core.blocks.StructBlock([('logo', wagtail.images.blocks.ImageChooserBlock(help_text='Logo', required=True)), ('background_color', wagtail.core.blocks.CharBlock(help_text='Numero hexadecimal del color de fondo (no incluir #) (si está vacio, se dejara en blanco)', required=False)), ('vertical_margin', wagtail.core.blocks.IntegerBlock(help_text='Cantidad (en pixeles) de espaciado vertical', required=False))])), ('title_dish_block', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(help_text='Titulo de la sección', max_length=50, required=True)), ('items', wagtail.core.blocks.ListBlock(streams.blocks.DishesStructBlock))]))], blank=True, null=True)),
                ('address', models.CharField(blank=True, max_length=100, null=True)),
                ('restaurant', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='restaurant.Restaurant')),
            ],
            options={
                'verbose_name': 'Restaurante',
                'verbose_name_plural': 'Restaurantes',
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='RestaurantsPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('content', wagtail.core.fields.StreamField([], blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'Restaurantes',
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='RestaurantPhones',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('phone', models.CharField(blank=True, max_length=15)),
                ('page', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='restaurant_phone', to='restaurant.RestaurantPage')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
    ]
