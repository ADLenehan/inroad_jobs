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
    return render(request, 'profile.html')


@login_required(login_url='/')
def home(request):
    return render_to_response('home.html')




