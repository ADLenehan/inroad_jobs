from django.contrib.auth.decorators import login_required
from django.shortcuts import render, render_to_response, redirect
from jobs.forms import PositionForm
from jobs.models import Position, Company
import requests, json, grequests, pprint
from django.contrib.auth import logout as auth_logout
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from lib.api import indeed


def home(request):

    context_dict = {}
    job_counter = 0
    job_ids = ""
    reqs = []
    json_txts = []
    job_list = {}

    try:
        positions = Position.objects.all()
        companies = Company.objects.all()

        for position in positions:
            if position.indeed_id:
                job_ids += position.indeed_id+","
                job_counter += 1

                if job_counter == 100:
                    job_counter = 0
                    reqs.append('http://api.indeed.com/ads/apigetjobs?publisher=454906352828196&jobkeys='
                         + job_ids + '&v=2&format=json')

        #reqs.append('http://api.indeed.com/ads/apigetjobs?publisher=454906352828196&jobkeys='+ job_ids + '&v=2&format=json')
        reqs.append('http://api.indeed.com/ads/apigetjobs?publisher=454906352828196&jobkeys='
                    + job_ids + '&v=2&format=json')
        rs = (grequests.get(u) for u in reqs)
        responses = grequests.map(rs)

        json = [response.json() for response in responses]

        for j in json:
            json_txts.append(j['results'])

        flat_list = {item['jobkey'] : item for sublist in json_txts for item in sublist}

        for position in positions:
            position.logo = position.company.logo
            position.color = position.company.color
            position.company_name = position.company.name
            print(position.logo)
            if position.indeed_id and flat_list[position.indeed_id]:
                position.job_title = flat_list[position.indeed_id]['jobtitle']
                position.city = flat_list[position.indeed_id]['city']
                position.state = flat_list[position.indeed_id]['state']
                position.description = flat_list[position.indeed_id]['snippet']
                position.url = flat_list[position.indeed_id]['url']
            elif position.indeed_id and not flat_list[position.indeed_id]:
                del position
            else:
                pass

        #pprint.pprint(flat_list)
        #print(positions[0].company)

        context_dict['positions'] = positions

    except Position.DoesNotExist:
        context_dict['positions'] = None

    return render(request, 'home.html', context_dict)


@login_required
def search(request):
    return render(request, "search.html")


@login_required
def add_position(request):
    form = PositionForm()

    if request.method == 'POST':
        form = PositionForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return home(request)
        else:
            print(form.errors)

    return render(request, 'add_position.html', {'position_form': form})