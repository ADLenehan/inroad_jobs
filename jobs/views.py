from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render, render_to_response, redirect, get_object_or_404, get_list_or_404
from django.forms.models import model_to_dict
from jobs.forms import PositionForm, CommentForm, BoardForm, ApplicationForm
from jobs.models import Position, Board, Comment, SavedJobs, Company, Application
from django.http import JsonResponse
from django.core.mail import EmailMessage
from django.shortcuts import redirect
from django.template import Context
from django.template.loader import get_template
import requests, json, grequests, pprint


@staff_member_required()
@login_required
def add_position(request, board_name):
    form = PositionForm()
    board_id = Board.objects.filter(slug=board_name)[0]
    new_position = Position(board=board_id)

    if request.method == 'POST':
        form = PositionForm(request.POST, instance= new_position)

        if form.is_valid():
            position = form.save(commit=True)
            return redirect('add_comment', board_name=board_id.slug,pk=position.pk)
        else:
            print(form.errors)

    return render(request, 'add_position.html', {'position_form': form})


def home(request):
    return redirect('/NY-tech/board')


def board(request, board_name):

    context_dict = {}
    job_counter = 0
    job_ids = ""
    reqs = []
    json_txts = []
    try:
        board_array = Board.objects.filter(slug=board_name)
    except Board.DoesNotExist:
        board_array = 0

    context_dict["board"] = board_array

    if board_array==0:
        try:
            positions = Position.objects.filter(board=board_array[0].pk)

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
                try:
                    position.job_title = flat_list[position.indeed_id]['jobtitle']
                    position.city = flat_list[position.indeed_id]['city']
                    position.state = flat_list[position.indeed_id]['state']
                    position.description = flat_list[position.indeed_id]['snippet']
                    position.url = flat_list[position.indeed_id]['url']
                except KeyError:
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


@staff_member_required()
@login_required
def add_board(request):
    form = BoardForm()

    if request.method == 'POST':
        form = BoardForm(request.POST)

        if form.is_valid():
            board = form.save(commit=True)
            board.author = request.user
            board.save()
            return redirect('home')
        else:
            print(form.errors)

    return render(request, 'add_board.html', {'board_form': form})


@staff_member_required()
@login_required
def add_comment(request, board_name, pk):
    form = CommentForm()
    position = Position.objects.get(pk=pk)
    new_comment = Comment(position=position)

    if request.method == "POST":
        form = CommentForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return redirect('home')
        else:
            print(form.errors)

    return render(request,'add_comment.html', {'comment_form': form})


def comments(request, board_name, pk):
    data = dict()
    saved = False
    position = Position.objects.get(pk=pk)
    data['position'] = model_to_dict(position)
    try:
        comments_obj = Comment.objects.get(position=pk)
        data['comments'] = (model_to_dict(comments_obj))
    except Comment.DoesNotExist:
        data['comments'] = False

    saved_jobs = SavedJobs.objects.filter(user=request.user)
    for job_obj in saved_jobs:
        if job_obj.position == position and job_obj.active == True:
            saved = True
            break
    data['saved']=saved

    return JsonResponse(data)


@login_required(login_url='/')
def save_job(request, pk):
    position = Position.objects.get(pk=pk)
    obj, created = SavedJobs.objects.update_or_create(user = request.user, position = position, defaults={"active": True})
    return redirect('board',board_name='NY-tech')


@login_required(login_url='/')
def unsave_job(request, pk):
    position = Position.objects.get(pk=pk)
    job = SavedJobs.objects.get(user = request.user, position = position)
    job.active=False
    job.save()
    return redirect('board', board_name='NY-tech')


@login_required(login_url='/')
def saved_jobs(request):

    positions = []
    context_dict = {}
    job_counter = 0
    job_ids = ""
    reqs = []
    json_txts = []

    jobs = SavedJobs.objects.filter(user=request.user, active=True)

    for job in jobs:
        position = Position.objects.get(pk=job.position.pk)
        position.applied = job.applied
        positions.append(position)
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

        for pos in positions:
            pos.logo = pos.company.logo
            pos.color = pos.company.color
            pos.company_name = pos.company.name
            try:
                pos.job_title = flat_list[pos.indeed_id]['jobtitle']
                pos.city = flat_list[pos.indeed_id]['city']
                pos.state = flat_list[pos.indeed_id]['state']
                pos.description = flat_list[pos.indeed_id]['snippet']
                pos.url = flat_list[pos.indeed_id]['url']
            except KeyError:
                del pos
            else:
                pass

        context_dict['positions'] = positions
    return render(request, 'saved_jobs.html', context_dict)


@login_required
def apply(request, pk):
    form = ApplicationForm()
    position = Position.objects.get(pk=pk)
    obj, created = SavedJobs.objects.update_or_create(user = request.user, position = position, defaults={"active": True, "applied": True})
    application = Application(user=request.user, position=position)

    if request.method == "POST" and request.user.is_authenticated():
        form = ApplicationForm(request.POST, instance=application)


        if form.is_valid():
            form.save(commit=True)
            user_data = request.user.social_auth.get(provider='linkedin-oauth2').extra_data
            question1 = request.POST.get('question1')
            question2 = request.POST.get('question2')

            template = get_template('add_position.txt')
            context = Context({
                'user_data': user_data,
                'question1': question1,
                'question2' : question2,
            })
            content = template.render(context)

            email = EmailMessage(
                "New application",
                content,
                'admin@inroad.co',
                ['andrew@inroad.co'])
            email.send()
            return redirect('saved_jobs')

        else:
            print(form.errors)

    return render(request,'application.html', {'application_form': form})
