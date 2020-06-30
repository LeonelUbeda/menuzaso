from django.db import models
from wagtail.admin.edit_handlers import (
    MultiFieldPanel,
    InlinePanel,
    FieldPanel
)
from wagtail.snippets.models import register_snippet
from django_extensions.db.fields import AutoSlugField
# Create your models here.


class MenuItem(Orderable):
    

@register_snippet
class Menu(ClusterableModel)
    title = models.CharField(max_length=100)
    slug = AutoSlugField(populate_from="title", editable=True)

    panels = [
        MultiFieldPanel([
            FieldPanel("title"),
            FieldPanel("slug"),
        
        ], heading="Menu")
        InlinePanel("menu_items", label="Menu Item")
    ]

    def __str__(self):
        return self.title