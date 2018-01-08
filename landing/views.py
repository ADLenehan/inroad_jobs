from django.http import HttpResponse

from django.shortcuts import render, redirect
from landing.forms import SignUpForm
from models import SignUp


def index(request):
    form = SignUpForm()

    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            site = form.cleaned_data['site']
            email = form.cleaned_data['email']
            signup = SignUp(site = site, email=email)
            signup.save()
            return redirect('thanks')
        else:
            print(form.errors)

    return render(request, 'landing/home.html', {'signup_form': form})
