from django import template

register = template.Library()

@register.filter
def addstring(s1,s2):
    return s1 + s2

register.filter("addstring",addstring)
