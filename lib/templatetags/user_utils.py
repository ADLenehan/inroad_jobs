from django import template

register = template.Library()

@register.assignment_tag()
def get_extra_data(request):
    if request.user and request.user.is_authenticated():
        user_data = request.user.social_auth.get(provider = 'linkedin-oauth2').extra_data
        return user_data
    else:
        return ''
