from django.contrib.auth.decorators import login_required
from django.shortcuts import render, render_to_response, redirect
from django.contrib.auth import logout as auth_logout
from django.http import HttpResponseRedirect

from django.http import HttpResponse


@login_required
def home(request):
    return render(request, 'home.html')


def logout(request):
    auth_logout(request)
    return redirect('/')