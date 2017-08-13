from django import template
import re
import math


register = template.Library()


def pager(context, page, request, *args, **kwargs):
# def pager(page, request):
    max_range = 10
    middle = int(math.ceil(max_range / 2))

    query_string = request.GET.urlencode()
    query_string = re.sub('&page(=[^&]*)?|^page(=[^&]*)?&?', '', query_string)
    base_url = request.path

    if not query_string:
        base_url = base_url + '?page='
    else:
        base_url = base_url + '?' + query_string + '&page='

    start_page = 1
    if page.number > middle and page.paginator.num_pages > max_range:
        start_page = page.number - middle

    end_page = start_page + max_range
    if start_page + max_range > page.paginator.num_pages:
        end_page = page.paginator.num_pages
        if (end_page - max_range) > 0:
            start_page = end_page - max_range + 1
    else:
        end_page = end_page - 1

    page_range = range(start_page, end_page + 1)

    return {'page': page, 'base_url': base_url, 'page_range': page_range}
# register.inclusion_tag('pager/pager.html', takes_context=True)(pager)
register.inclusion_tag('pager/pager.html', takes_context=True)(pager)