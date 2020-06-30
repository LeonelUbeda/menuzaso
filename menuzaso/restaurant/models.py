from django.db import models, signals
from wagtail.core.models import Page
from wagtail.core import blocks as wagtailBlocks
from django.core.exceptions import ValidationError
from wagtail.core.fields import RichTextField, StreamField
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel, MultiFieldPanel, StreamFieldPanel, InlinePanel
from streams import blocks
from django.utils.translation import gettext_lazy as _
from django.utils.text import slugify
from user.models import User
# Create your models here.


class Restaurant(models.Model):
    name = models.CharField(max_length=60, blank=False, null=True)
    staff = models.ManyToManyField(User, related_name='restaurants')
    slug = models.SlugField(max_length=50, blank=False, null=False)
    
    def clean(self):
        #import pdb; pdb.set_trace()
        cleaned_data = super().clean()
        if not self.id:
            #Si se está creando el restaurante, entonces se verifica si el slug no está siendo ocupado 
            #por algun otro restaurante
            restaurant = RestaurantPage.objects.filter(slug=self.slug)
            if restaurant.exists():
                raise ValidationError(_("Ya existe ese slug"))
            #Mejorar esto
            #Se obtiene la pagina padre "restaurantes"
            parent = RestaurantsPage.objects.get(slug='restaurantes')
            #Se crea la instancia de una pagina tipo RestaurantPage
            restaurant = RestaurantPage(slug=self.slug, title=self.name)
            #Luego la instancia restaurante se añade como hijo de la pagina RestaurantsPage
            parent.add_child(instance=restaurant)
        else: 
            #Si se editó la instancia y se está cambiando el slug entonces
            # hacemos unas verificaciones
            if self.slug != self.__original_slug:
                #Si ya existe una pagina tipo RestaurantPage con el slug
                if RestaurantPage.objects.filter(slug=self.slug).exists():
                    raise ValidationError(_("Ya existe ese slug"))
                else:
                    restaurant = RestaurantPage.objects.get(slug=self.__original_slug)
                    restaurant.slug = self.slug
                    restaurant.save()


    def __init__(self, *args, **kwargs):
        super(Restaurant, self).__init__(*args, **kwargs)
        self.__original_slug = self.slug
    def __str__(self):
        return self.name


class RestaurantsPage(Page):
    template = 'restaurant/restaurants_page.html'
    max_count = 1
    
    content = StreamField(
        [
            ("ritch_block", blocks.RichTextBlock())
        ],
        null=True,
        blank=True
    )
    content_panels = Page.content_panels + [
        StreamFieldPanel("content")
    ]
    class Meta:
        verbose_name_plural = "Restaurantes"



class RestaurantPage(Page):
    template = 'restaurant/restaurant_page.html'
    content = StreamField(
        [
            ("category_block", blocks.CategoryBlock()),
            ("ritch_block", blocks.RichTextBlock())
        ],
        null=True,
        blank=True,
    )
    subpage_types = []
    parent_page_types = ['restaurant.RestaurantsPage']
    restaurant = models.ForeignKey(Restaurant, null=True, on_delete=models.SET_NULL, blank=True)
    is_creatable = False
    promote_panels = [
        MultiFieldPanel([
            # Disable slug
            #FieldPanel('slug'),
            FieldPanel('seo_title'),
            #FieldPanel('show_in_menus'),
            FieldPanel('search_description'),
        ], _('Common page configuration')),
    ]

    content_panels = promote_panels + [

            FieldPanel('title', classname="full title"),
            StreamFieldPanel("content", classname="restaurant-fields")
       
    ]

    parent_page_types = ['RestaurantsPage']

    

    class Meta:
        verbose_name = "Restaurante"
        verbose_name_plural = "Restaurantes"

"""
class Category(models.Model):
    name = models.CharField(max_length=60, blank=False, null=True)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)

class Dish(models.Model):
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True, blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    price = models.IntegerField()
    USD = 'USD'
    NIO = 'NIO'
    CURRENCY_CHOICES = [
        (USD, 'Dolares'),
        (NIO, 'Cordobas')
    ]
    currency = models.CharField(max_length=3, choices=CURRENCY_CHOICES, default=NIO)
    ingredients = StreamField([('ingredientes', wagtailBlocks.ListBlock(blocks.IngredientsStructBlock))])

"""
from django.db.models.signals import post_save
from django.dispatch import receiver
@receiver(post_save, sender=Restaurant)
def post_save_restaurant(sender, instance, created, *args, **kwargs):
    if created:
        print('HOLAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA')

