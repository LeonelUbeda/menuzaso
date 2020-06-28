from django.db import models

from wagtail.core.models import Page


class HomePage(Page):
    templates = 'templates/home/home_page.html'
    max_count = 1

