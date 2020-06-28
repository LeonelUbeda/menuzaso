from django.db import models
from wagtail.core.models import Page
from wagtail.core.fields import RichTextField, StreamField
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from streams import blocks
# Create your models here.



class Restaurant(models.Model):
    name = models.CharField(max_length=60, blank=False, null=True)

    def __str__(self):
        return self.name



class Category(models.Model):
    name = models.CharField(max_length=60, blank=False, null=True)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)



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
        blank=True
    )
    content_panels = Page.content_panels + [
        StreamFieldPanel("content")
    ]

    parent_page_types = ['RestaurantsPage']
    class Meta:
        verbose_name = "Restaurante"
        verbose_name_plural = "Restaurantes"


