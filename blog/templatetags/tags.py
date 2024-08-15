from django import template
from ..models import Post
from django.contrib.auth.models import User
register = template.Library()


@register.simple_tag
def count_tag(query):
    return query.count()