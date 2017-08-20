from django.contrib.auth.decorators import login_required
from django.shortcuts import render, render_to_response, redirect, get_object_or_404, get_list_or_404
from jobs.forms import PositionForm, CommentForm
from jobs.models import Position, Board, Comment
import requests, json, grequests, pprint
from django.contrib.auth import logout as auth_logout
from django.http import HttpResponseRedirect, JsonResponse
from django.http import HttpResponse
from lib.api import indeed


def home(request):

    context_dict = {}
    job_counter = 0
    job_ids = ""
    reqs = []
    json_txts = []

    try:
        #board = Board.objects.filter(author=request.user)
        #positions = Position.objects.filter(board=board)
        positions = Position.objects.all()


        for position in positions:
            if position.indeed_id:
                job_ids += position.indeed_id+","
                job_counter += 1

                if job_counter == 100:
                    job_counter = 0
                    reqs.append('http://api.indeed.com/ads/apigetjobs?publisher=454906352828196&jobkeys='
                         + job_ids + '&v=2&format=json')

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
            position = form.save(commit=True)
            return redirect('add_comment', position.pk)
        else:
            print(form.errors)

    return render(request, 'add_position.html', {'position_form': form})

@login_required
def add_comment(request, pk):
    form = CommentForm()
    position = get_object_or_404(Position, pk=pk)

    if request.method == "POST":
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.position = position
            comment.save()
            return redirect('home')
        else:
            form = CommentForm()

    return render(request,'add_comment.html', {'comment_form': form})


def comments(request, pk):

    try:
        comments_obj = Comment.objects.filter(position=pk).order_by('created_on').values('author','text')

    except Comment.DoesNotExist:
        comments_obj = None

    return JsonResponse({'results': list(comments_obj)})

