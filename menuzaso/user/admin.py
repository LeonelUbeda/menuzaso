from django import forms
from django.utils.translation import ugettext_lazy as _
from restaurant.models import Restaurant
from wagtail.users.forms import UserEditForm, UserCreationForm



class CustomUserEditForm(UserEditForm):
    restaurant = forms.ModelChoiceField(queryset=Restaurant.objects.all(), required=True, label=_("Restaurante"))



class CustomUserCreationForm(UserCreationForm):
    restaurant = forms.ModelChoiceField(queryset=Restaurant.objects.all(), required=True, label=_("Restaurante"))



