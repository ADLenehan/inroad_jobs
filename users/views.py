from django.shortcuts import render_to_response, redirect, render
from django.contrib.auth.decorators import login_required
from django.template.context import RequestContext
from django.contrib.auth import logout as auth_logout


def logout(request):
    auth_logout(request)
    return redirect('/')


def login(request):
    return render_to_response('login.html', context=RequestContext(request))


@login_required(login_url='/')
def profile(request):
    if request.user and request.user.is_authenticated():
        user_data = request.user.social_auth.get(provider = 'linkedin-oauth2').extra_data
        return render(request, 'profile.html', user_data)
    else:
        return ''

@login_required(login_url='/')
def home(request):
    return render_to_response('home.html')




