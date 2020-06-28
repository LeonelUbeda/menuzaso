from django.db import models, signals
from wagtail.core.models import Page
from wagtail.core.fields import RichTextField, StreamField
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel, MultiFieldPanel, StreamFieldPanel, InlinePanel
from streams import blocks
from django.utils.text import slugify
from user.models import User
# Create your models here.








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
    content_panels = Page.content_panels + [
        StreamFieldPanel("content", classname="collapsible")
    ]

    parent_page_types = ['RestaurantsPage']
    class Meta:
        verbose_name = "Restaurante"
        verbose_name_plural = "Restaurantes"



class Restaurant(models.Model):
    name = models.CharField(max_length=60, blank=False, null=True)
    #staff = models.ManyToManyField(User)
    slug = models.SlugField(max_length=50, blank=False, null=False)

    def save(self, *args, **kwargs):
        #page is new
        if not self.id:
            parent = RestaurantsPage.objects.get(slug='restaurantes').specific
            restaurant = RestaurantPage(slug=self.slug, title=self.name)
            parent.add_child(instance=restaurant)
        else: 
            
        super(Restaurant, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=60, blank=False, null=True)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)



from django.db.models.signals import post_save
from django.dispatch import receiver
@receiver(post_save, sender=Restaurant)
def post_save_restaurant(sender, instance, created, *args, **kwargs):
    if created:
        print('HOLAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA')

