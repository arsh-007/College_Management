# Create your views here.
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from .forms import Ancform, LoginForm, PollQuestion, SingUpForm, QuizForm, Addchoices
from django.contrib.auth import authenticate, login, logout
from .models import Announcement, quiz, User, Question, Choice
from django.db.models import Q
import datetime
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from .models import Question, Choice, Vote
from django.contrib import messages
from django.views import generic

# Create your views here.


@login_required(login_url='/login/')
def home(request):
    profile_email = request.user.email
    profile_year = profile_email[-14:-12]
    profile_department = profile_email[-17:-14]
    now = datetime.datetime.now()
    if request.user.is_authenticated:

        upcomingQuiz = quiz.objects.filter(
            Q(branch=profile_department) | Q(branch="ALL")).filter(Q(year=profile_year) | Q(year="ALL")).filter(start_time__gt=now).order_by('date_posted')
        Quizpast = quiz.objects.filter(
            Q(branch=profile_department) | Q(branch="ALL")).filter(Q(year=profile_year) | Q(year="ALL")).filter(end_time__lt=now).order_by('date_posted')
        Quiznow = quiz.objects.filter(
            Q(branch=profile_department) | Q(branch="ALL")).filter(Q(year=profile_year) | Q(year="ALL")).filter(start_time__lte=now).filter(end_time__gte=now).order_by('date_posted')
        Announcements = Announcement.objects.filter(
            Q(branch=profile_department) | Q(branch="ALL")).filter(Q(year=profile_year) | Q(year="ALL")).order_by('date')
        return render(request, 'main/home.html', {'Qfuture': upcomingQuiz, 'Qpast': Quizpast, 'Qpresent': Quiznow, 'A': Announcements})
    else:
        return HttpResponseRedirect('/login/')


# Create your views here.


def dashboard(request):
    if request.user.is_authenticated and request.user.profile.is_professor:

        Quizs = quiz.objects.filter(posted_by_id=request.user.id)
        Announcements = Announcement.objects.all()
        Polls = Question.objects.filter(posted_by_id=request.user.id)
        return render(request, 'main/dashboard.html', {'Quizs': Quizs, 'A': Announcements, 'polls': Polls})
    else:
        messages.success(request, "You can not access Dashboard")
        return HttpResponseRedirect('/')

# Create your views here.


def user_login(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = LoginForm(request=request, data=request.POST)
            if form.is_valid():
                uname = form.cleaned_data['username']
                upass = form.cleaned_data['password']
                user = authenticate(username=uname, password=upass)
                if user is not None:
                    login(request, user)
                    return HttpResponseRedirect('/')
                else:

                    return HttpResponseRedirect('/login/')
            else:
                messages.error(request, "Invalid Username or Password")
                return HttpResponseRedirect('/login/')

        else:
            form = LoginForm
            return render(request, 'main/login.html', {'form': form})

    else:
        return HttpResponseRedirect('/')


# Create your views here.


def user_singup(request):
    if request.method == "POST":
        form = SingUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('login')

    else:
        form = SingUpForm()
    return render(request, 'main/singup.html', {'form': form})


# Create your views here.


def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')


def add_quiz(request):
    if request.user.is_authenticated and request.user.profile.is_professor:

        if request.method == 'POST':
            form = QuizForm(request.POST)
            if form.is_valid():
                posted_by = request.user
                subcode = form.cleaned_data['subcode']
                branch = form.cleaned_data['branch']
                year = form.cleaned_data['year']
                quizurl = form.cleaned_data['quizurl']
                start_time = form.cleaned_data['start_time']
                end_time = form.cleaned_data['end_time']
                desc = form.cleaned_data['desc']
                qz = quiz(subcode=subcode, branch=branch, year=year, posted_by=posted_by,
                          quizurl=quizurl, start_time=start_time, end_time=end_time, desc=desc)
                qz.save()
                form = QuizForm()
        else:
            form = QuizForm()
        return render(request, 'main/addquiz.html', {'form': form})
    else:
        return HttpResponseRedirect('/login/')


def add_anc(request):
    if request.user.is_authenticated and request.user.profile.is_professor:

        if request.method == 'POST':
            form = Ancform(request.POST)
            if form.is_valid():
                posted_by = request.user
                subcode = form.cleaned_data['subcode']
                branch = form.cleaned_data['branch']
                year = form.cleaned_data['year']
                title = form.cleaned_data['title']
                desc = form.cleaned_data['desc']
                announce = Announcement(posted_by=posted_by, subcode=subcode, branch=branch, year=year,
                                        title=title, desc=desc)
                announce.save()
                form = Ancform()
        else:
            form = Ancform()
        return render(request, 'main/addannouncement.html', {'form': form})
    else:
        return HttpResponseRedirect('/login/')


def update_quiz(request, id):
    if request.user.is_authenticated and request.user.profile.is_professor:
        if request.method == 'POST':
            pi = quiz.objects.get(pk=id)
            form = QuizForm(request.POST, instance=pi)
            if form.is_valid():
                form.save()
        else:
            pi = quiz.objects.get(pk=id)
            form = QuizForm(instance=pi)
        return render(request, 'main/updatequiz.html', {'form': form})

    else:
        return HttpResponseRedirect('/login/')


def delete_quiz(request, id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            pi = quiz.objects.get(pk=id)
            pi.delete()
            return HttpResponseRedirect('/dashboard/')
    else:
        return HttpResponseRedirect('/login/')


@login_required(login_url='/login/')
def pollindex(request):
    profile_email = request.user.email
    profile_year = profile_email[-14:-12]
    profile_department = profile_email[-17:-14]
    now = datetime.datetime.today()
    polls = Question.objects.filter(Q(branch=profile_department) | Q(branch="ALL")).filter(
        Q(year=profile_year) | Q(year="ALL")).filter(start_date__lte=now).filter(end_date__gte=now)
    pollsdone = Question.objects.filter(Q(branch=profile_department) | Q(branch="ALL")).filter(
        Q(year=profile_year) | Q(year="ALL")).filter(end_date__lt=now)
    return render(request, 'main/index.html', {'p': polls, 'q': pollsdone})


def addpoll(request):
    if request.user.is_authenticated and request.user.profile.is_professor:

        if request.method == 'POST':
            form = PollQuestion(request.POST)
            if form.is_valid():
                posted_by = request.user
                question_text = form.cleaned_data['question_text']
                branch = form.cleaned_data['branch']
                year = form.cleaned_data['year']
                title = form.cleaned_data['title']
                start_date = form.cleaned_data['start_date']
                end_date = form.cleaned_data['end_date']
                pub_date = datetime.date.today()

                announce = Question(posted_by=posted_by, question_text=question_text, branch=branch, year=year,
                                    title=title, start_date=start_date, end_date=end_date, pub_date=pub_date)
                announce.save()

                new_choice1 = Choice(
                    question=announce, choice_text=form.cleaned_data['choice1']).save()
                new_choice2 = Choice(
                    question=announce, choice_text=form.cleaned_data['choice2']).save()

                form = PollQuestion()
        else:
            form = PollQuestion()
        return render(request, 'main/addpoll.html', {'form': form})
    else:
        return HttpResponseRedirect('/login/')


def vote(request, id):
    profile_email = request.user.email
    profile_year = profile_email[-14:-12]
    profile_department = profile_email[-17:-14]
    now = datetime.datetime.today()
    question = Question.objects.get(pk=id)
    options = question.choices.all()
    if request.method == "POST":
        if Vote.objects.filter(voter=request.user, question=question).exists():
            messages.error(
                request, "You can not vote now because you have already voted on this poll")
            polls = Question.objects.filter(Q(branch=profile_department) | Q(branch="ALL")).filter(
                Q(year=profile_year) | Q(year="ALL")).filter(start_date__lte=now).filter(end_date__gte=now)
            pollsdone = Question.objects.filter(Q(branch=profile_department) | Q(branch="ALL")).filter(
                Q(year=profile_year) | Q(year="ALL")).filter(end_date__lt=now)
            return render(request, 'main/index.html', {'p': polls, 'q': pollsdone})
        else:
            Vote.objects.create(voter=request.user, question=question)
            value = request.POST['choice']
            selected_option = options.get(id=value)
            selected_option.votes += 1
            selected_option.save()

    return render(request, 'main/vote.html', {'question': question, 'options': options})


def result(request, id):
    question = Question.objects.get(pk=id)
    options = Choice.objects.filter(question_id=id)
    totalvotes = int(0)
    for option in options:
        totalvotes += option.votes
    for option in options:
        option.votes = (option.votes/totalvotes)*100

    return render(request, 'main/result.html', {'question': question, 'options': options})


def addchoice(request, id):
    if request.user.is_authenticated:

        if request.method == 'POST':
            pi = Question.objects.get(pk=id)
            form = Addchoices(request.POST)
            if form.is_valid():

                newchoice = form.cleaned_data['choice_text']
                choice = Choice(question_id=id, choice_text=newchoice)
                choice.save()
        else:
            form = Addchoices()
        return render(request, 'main/addchoices.html', {'form': form})
    else:
        return HttpResponseRedirect('/login/')