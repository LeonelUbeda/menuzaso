from django.contrib import admin
from wagtail.contrib.modeladmin.options import (
    ModelAdmin,
    modeladmin_register,
)
from .models import Restaurant
# Register your models here.



class RestaurantAdmin(ModelAdmin):
    model = Restaurant
    menu_label = 'Restaurants'
    menu_icon = 'Placeholder'
    menu_order = 200
    add_to_settings_menu = False
    exclude_from_explore = False
    list_display = ('name', 'id',)
    search_fields = ('name',)


modeladmin_register(RestaurantAdmin)