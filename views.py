# Create your views here.
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponseRedirect, redirect
from .forms import Ancform, LoginForm, SingUpForm, QuizForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import Announcement, quiz, User
from django.conf import settings
import datetime


# Create your views here.

def home(request):
    profile_email = request.user.email
    profile_year = profile_email[-14:-12]
    profile_department = profile_email[-17:-14]
    now = datetime.datetime.now()
    if request.user.is_authenticated:
        Quiz = quiz.objects.filter(
            branch=profile_department).filter(year=profile_year).order_by('date_posted')
        return render(request, 'main/home.html', {'Quiz': Quiz})
    else:
        return HttpResponseRedirect('/login/')


# Create your views here.


def dashboard(request):
    if request.user.is_authenticated and request.user.is_professor:

        Quizs = quiz.objects.all()
        Announcements = Announcement.objects.all()
        return render(request, 'main/dashboard.html', {'Quizs': Quizs, 'A': Announcements})
    else:
        ValueError("You are not allowed to Dashboard")
        return HttpResponseRedirect('/login/')


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
                    messages.success(request, "loged in successfully")
                    return HttpResponseRedirect('/')
        else:
            form = LoginForm
            return render(request, 'main/login.html', {'form': form})

    else:
        return HttpResponseRedirect('/dashboard/')


# Create your views here.


def user_singup(request):
    if request.method == "POST":
        form = SingUpForm(request.POST)
        if form.is_valid():
            messages.success(request, "You are singed in as a student.")
            user = form.save()

            return redirect('login')

    else:
        form = SingUpForm()
    return render(request, 'main/singup.html', {'form': form})


# Create your views here.


def user_logout(request):
    logout(request)

    return HttpResponseRedirect('/')


def add_quiz(request):
    if request.user.is_authenticated:

        if request.method == 'POST':
            form = QuizForm(request.POST)
            if form.is_valid():
                posted_by = request.user
                subcode = form.cleaned_data['subcode']
                branch = form.cleaned_data['branch']
                year = form.cleaned_data['year']
                date = form.cleaned_data['date']
                quizurl = form.cleaned_data['quizurl']
                start_time = form.cleaned_data['start_time']
                end_time = form.cleaned_data['end_time']
                desc = form.cleaned_data['desc']
                date_posted = datetime.date.today()
                qz = quiz(subcode=subcode, branch=branch, year=year, posted_by=posted_by, date_posted=date_posted,
                          date=date, quizurl=quizurl, start_time=start_time, end_time=end_time, desc=desc)
                qz.save()
                form = QuizForm()
        else:
            form = QuizForm()
        return render(request, 'main/addquiz.html', {'form': form})
    else:
        return HttpResponseRedirect('/login/')


def add_anc(request):
    if request.user.is_authenticated:

        if request.method == 'POST':
            form = Ancform(request.POST)
            if form.is_valid():
                posted_by = request.user
                subcode = form.cleaned_data['subcode']
                branch = form.cleaned_data['branch']
                year = form.cleaned_data['year']
                date = form.cleaned_data['date']
                title = form.cleaned_data['title']
                desc = form.cleaned_data['desc']
                announce = Announcement(posted_by=posted_by, subcode=subcode, branch=branch, year=year,
                                        date=date, title=title, desc=desc)
                announce.save()
                form = Ancform()
        else:
            form = Ancform()
        return render(request, 'main/addannouncement.html', {'form': form})
    else:
        return HttpResponseRedirect('/login/')


def update_quiz(request, id):
    if request.user.is_authenticated:
        return render(request, 'main/updatequiz.html')
    else:
        return HttpResponseRedirect('/login/')


def delete_quiz(request, id):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/dashboard/')
    else:
        return HttpResponseRedirect('/login/')
