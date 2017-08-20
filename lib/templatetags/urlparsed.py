from django import template
from urllib.parse import urlparse

register = template.Library()

@register.filter
def urlparsed(url, response):
    """Gets the domain name from the url"""

    if not url.startswith('http'):
        url = '%s%s' % ('http://', url)

    parsed = urlparse(url)

    return getattr(parsed, response)

@register.filter
def urlparsed_file_name(url):
    """Gets the file name element from a url"""

    parsed = urlparse(url)

    return parsed.path.split('/')[-1]