from django.contrib import admin
from wagtail.core import hooks
from django.utils.safestring import mark_safe
from wagtail.contrib.modeladmin.views import CreateView
from django import forms
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.admin.edit_handlers import (
    InlinePanel,
    FieldPanel,
    StreamFieldPanel
)
from wagtail.admin.forms import WagtailAdminModelForm
from wagtail.contrib.modeladmin.options import (
    ModelAdmin,
    modeladmin_register,
)
from .models import Restaurant, RestaurantPage
# Register your models here.



"""
class RestaurantPageform(ModelAdmin):
    model = RestaurantPage
    menu_label = 'Restaurantes paginas'
    menu_icon = 'Placeholder'
    menu_order = 200
    def save():
        print('NEOP')
    
    def save_model(self, request, obj, form, change):
        print('HOLAAAAAAAAAAAAAAAA')
"""



class RestaurantAdmin(ModelAdmin):
    model = Restaurant
    menu_label = 'Restaurants'
    menu_icon = 'Placeholder'
    menu_order = 200
    add_to_settings_menu = False
    exclude_from_explore = False
    list_display = ('name', 'id',)
    search_fields = ('name', 'slug')
    panels = [
        FieldPanel('name', classname="full title"),
        FieldPanel('slug'),
        FieldPanel('staff', widget=forms.CheckboxSelectMultiple)
    ]

"""
class DishAdmin(ModelAdmin):
    model = Dish
    menu_label = 'Dishes'
    menu_icon = 'Placeholder'
    menu_order = 300
    add_to_settings_menu = False
    exclude_from_explore = False
    list_display = ('name', 'id',)
    search_fields = ('name')
    panels = [
        FieldPanel('name', classname="full title"),
        ImageChooserPanel('image'),
        FieldPanel('price'),
        FieldPanel('currency'),
        StreamFieldPanel('ingredients')
    ]

    def clean(holap):
        print('CHAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAALI')
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        # Only show people managed by the current user
        return qs
"""

@hooks.register('construct_image_chooser_queryset')
def show_my_uploaded_image_only(images, request):
    if(request.user.is_superuser):
        return images
    return images.filter(uploaded_by_user=request.user)


class WelcomePanel:
    order = 50

    def render(self):
        return mark_safe("""
        <section class="panel summary nice-padding">
          <h3>No, but seriously -- welcome to the admin homepage.</h3>
        </section>
        """)

@hooks.register('construct_homepage_panels')
def add_another_welcome_panel(request, panels):
    #if request.user.is_superuser:
    panels.append(WelcomePanel())





from django.templatetags.static import static
from django.utils.html import format_html
from wagtail.core import hooks



@hooks.register('insert_global_admin_css', order=100)
def global_admin_css():
    return format_html('<link rel="stylesheet" href="{}">', static("css/custom.css"))

modeladmin_register(RestaurantAdmin)