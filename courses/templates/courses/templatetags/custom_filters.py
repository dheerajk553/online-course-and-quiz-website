from django import template
register = template.Library()

@register.filter
def get_option(quiz, index):
    return getattr(quiz, f'option{index}')
