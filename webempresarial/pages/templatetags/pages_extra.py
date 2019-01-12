# https://docs.djangoproject.com/en/2.0/howto/custom-template-tags/
from django import template
from pages.models import Page

register = template.Library()


@register.simple_tag
def get_page_list():
    pages = Page.objects.all()
    return pages
