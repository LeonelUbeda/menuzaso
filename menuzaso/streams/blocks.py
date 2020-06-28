""" Streamfields """
from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock





class CategoryBlock(blocks.StructBlock):
    title = blocks.CharBlock(required=True, help_text='Add your tittle')
    text = blocks.TextBlock(required=True, help_text='Add text')

    dishes = blocks.ListBlock(
        blocks.StructBlock(
            [
                ("image", ImageChooserBlock(required=False)),
                ("title", blocks.CharBlock(required=True, max_length=50)),
                ("description", blocks.CharBlock(required=False, max_length=100)),
                ("components", blocks.ListBlock(
                    blocks.StructBlock(
                        [
                            ("name", blocks.CharBlock(required=True)),
                            ("quantity", blocks.CharBlock(required=True)),
                            ("price", blocks.FloatBlock(required=True)),
                            ("currency", blocks.ChoiceBlock(choices=[
                                ("C$", "Cordoba Nicaraguense"), ("$", "Dolar estadounidense")
                                ], required=True))
                        ]
                    )
                ))
            ]
        )
    )
    class Meta:
        template = "streams/category_block.html"
        icon = "edit"
        label = "Category"



class RichTextBlock(blocks.RichTextBlock):
    class Meta:
        template = "streams/rich_text_block.html"
        icon = "edit"
        label = "Full RichText"

