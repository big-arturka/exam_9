from django import template

register = template.Library()


@register.filter
def fav_by(obj, user):
    return obj.fav_by(user)
