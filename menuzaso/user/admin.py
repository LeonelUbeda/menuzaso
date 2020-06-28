from django import forms
from django.utils.translation import ugettext_lazy as _
#from restaurant.models import Restaurant
from wagtail.users.forms import UserEditForm, UserCreationForm


    #description = forms.ModelChoiceField(queryset=Restaurant.objects.all(), required=True, label=_("Restaurante"))

class CustomUserEditForm(UserEditForm):
    description = forms.CharField(required=False, label=_("Description for user"))


class CustomUserCreationForm(UserCreationForm):
    description = forms.CharField(required=False, label=_("Description for user"))



