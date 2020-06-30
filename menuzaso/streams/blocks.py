""" Streamfields """
from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock


class IngredientsStructBlock(blocks.StructBlock):
    name = blocks.CharBlock(required=True)
    quantity = blocks.CharBlock(required=True)
    class Meta:
        form_classname = 'ingredients-list'



class DishesStructBlock(blocks.StructBlock):
    image = ImageChooserBlock(required=False)
    title = blocks.CharBlock(required=True, max_length=50)
    description = blocks.CharBlock(required=False, max_length=100)
    price = blocks.FloatBlock(required=True)
    currency = blocks.ChoiceBlock(choices=[
        ("C$", "Cordoba Nicaraguense"), ("$", "Dolar estadounidense")
    ], required=True)
    ingredients = blocks.CharBlock(required=False, max_length=100)
    class Meta:
        icon = "folder"




class CategoryBlock(blocks.StructBlock):
    title = blocks.CharBlock(required=True, help_text='Nombre de la categoria')
    background = ImageChooserBlock(required=True, help_text='Imagen de fondo de categoria')
    dishes = blocks.ListBlock(DishesStructBlock)
    class Meta:
        template = "streams/category_block.html"
        icon = "edit"
        label = "Category"



class RichTextBlock(blocks.RichTextBlock):
    class Meta:
        template = "streams/rich_text_block.html"
        icon = "edit"
        label = "Full RichText"

