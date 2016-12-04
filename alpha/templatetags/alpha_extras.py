from django import template
from django.template.defaultfilters import stringfilter
from django.utils.safestring import mark_safe
import re

register = template.Library()

__regex__ = re.compile('(?P<line>.*)(\r\n)*')

@register.filter(name='paralize')
@stringfilter
def paralize(value):
    pile = ''
    for str in __regex__.finditer(value):
        if(str.group('line') != ''):
            pile += ('<p>'+str.group('line')+'</p>')
    return mark_safe(pile)

# the directory has to be named
# templatetags
# apparently this is hard coded!!