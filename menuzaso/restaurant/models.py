from django.db import models, signals
from wagtail.core.models import Page
from wagtail.core import blocks as wagtailBlocks
from django.core.exceptions import ValidationError
from wagtail.core.fields import RichTextField, StreamField
from django.conf import settings
from wagtail.admin.edit_handlers import (
    FieldPanel, 
    StreamFieldPanel, 
    MultiFieldPanel, 
    StreamFieldPanel, 
    InlinePanel, 
    ObjectList, 
    TabbedInterface,
)

from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.core.models import Orderable
from modelcluster.fields import ParentalKey
from streams import blocks
from django.utils.translation import gettext_lazy as _
from django.utils.text import slugify
from user.models import User
from wagtail.snippets.models import register_snippet
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
    
    content = StreamField([],null=True,blank=True)
    content_panels = Page.content_panels + [
        StreamFieldPanel("content")
    ]
    class Meta:
        verbose_name_plural = "Restaurantes"



class RestaurantPhones(Orderable):
    page = ParentalKey("restaurant.RestaurantPage", related_name="restaurant_phone")
    phone = models.CharField(max_length=15, blank=True, null=False)
    panels = [FieldPanel("phone")]


class DishOrderable(Orderable):
    """ Para seleccionar los platillos del snippet Dish """
    

class Dish(models.Model):
    managed_by = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=False)
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
    ingredients = models.CharField(max_length=100, blank=True, null=True)
    # ingredients = StreamField([('ingredientes', wagtailBlocks.ListBlock(blocks.IngredientsStructBlock))])

    panels = [
        MultiFieldPanel(
            [
                FieldPanel("name"),
                ImageChooserPanel("image"),
                FieldPanel("currency"),
                FieldPanel("ingredients"),
                FieldPanel("price")
            ],
            heading="Dish"
        )
    ]

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Dish"
        verbose_name_plural = "Dishes"

# register_snippet(Dish)


class RestaurantPage(Page):
    template = 'restaurant/restaurant_page.html'
    content = StreamField(
        [
            ("category_block", blocks.CategoryBlock()),
            ("logo_block", blocks.LogoBlock()),
            ("title_dish_block", blocks.TitleDish())
        ],
        null=True,
        blank=True,
    )

    address = models.CharField(max_length=100, null=True, blank=True)
    restaurant = models.ForeignKey(Restaurant, null=True, on_delete=models.SET_NULL, blank=True)

    subpage_types = []
    parent_page_types = ['restaurant.RestaurantsPage']

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

    details_panels = [
        MultiFieldPanel([
            FieldPanel('address'),
            InlinePanel("restaurant_phone", max_num=5, min_num=1, label="Phones")
        ], _('Details'))
    ]
    content_panels = [
            FieldPanel('title', classname="full title"),
            StreamFieldPanel("content", classname="restaurant-fields")
       
    ]

    edit_handler = TabbedInterface(
        [
            ObjectList(content_panels, heading='Content'),
            ObjectList(promote_panels, heading='Promotional stuff'),
            ObjectList(details_panels, heading='Contacto'), 

        ]
    )
    parent_page_types = ['RestaurantsPage']

    class Meta:
        verbose_name = "Restaurante"
        verbose_name_plural = "Restaurantes"





from django.db.models.signals import post_save
from django.dispatch import receiver
@receiver(post_save, sender=Restaurant)
def post_save_restaurant(sender, instance, created, *args, **kwargs):
    if created:
        print('HOLAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA')

