from django.db.models.fields import DateField, DateTimeField
from django.forms import widgets, ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from django.utils.regex_helper import Choice
from .models import Announcement, User, quiz
from . models import BRANCH_CHOICES, YEAR_CHOICES
from main.models import quiz
import datetime


class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(
        attrs={'autofocus': True, 'class': 'form-control'}))
    password = forms.CharField(label=('password'), strip=False, widget=forms.PasswordInput(
        attrs={'autocomplete': True, 'class': 'form-control'}))


class SingUpForm(UserCreationForm):
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control"}))
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control"}))

    username = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control"}))
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control"}))
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control"}))
    email = forms.CharField(widget=forms.TextInput(
        attrs={"class": "form-control"}))

    class Meta(UserCreationForm):
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1',
                  'password2', 'branch', 'year', 'RollNo')
        widgets = {'branch': forms.RadioSelect(
            choices=BRANCH_CHOICES),
            'year': forms.RadioSelect(
            choices=YEAR_CHOICES),
        }


class QuizForm (forms.ModelForm):
    class Meta:
        model = quiz
        fields = ['subcode', 'branch', 'year', 'date',
                  'start_time', 'end_time', 'quizurl', 'desc']
        labels = {'subcode': 'Subject code', 'branch': 'Branch', 'year': 'Year',
                  'quizurl': 'Link', 'date': 'Date', 'start_time': 'Starting Time', 'end_time': 'Ending Time', 'desc': 'Description'}
        widgets = {'subcode': forms.TextInput(attrs={"class": "form-control"}),
                   'branch': forms.Select(choices=BRANCH_CHOICES, attrs={"class": "form-control"}),
                   'year': forms.Select(choices=YEAR_CHOICES, attrs={"class": "form-control"}),

                   'date': forms.SelectDateWidget(),
                   'start_time': forms.TimeInput(attrs={'type': 'time'}, format='%H:%M'),
                   'end_time': forms.TimeInput(attrs={'type': 'time'}, format='%H:%M'),
                   'quizurl': forms.URLInput(attrs={"class": "form-control"}),
                   'desc': forms.Textarea(attrs={"class": "form-control"}), }


class Ancform (forms.ModelForm):
    class Meta:
        model = Announcement
        fields = ['title', 'subcode', 'branch', 'year', 'date',
                  'desc']
        labels = {'title': 'Title', 'subcode': 'Subject code', 'branch': 'Branch', 'year': 'Year',
                  'date': 'Date',  'desc': 'Description'}
        widgets = {'title': forms.TextInput(attrs={"class": "form-control"}),
                   'subcode': forms.TextInput(attrs={"class": "form-control"}),
                   'branch': forms.Select(choices=BRANCH_CHOICES, attrs={"class": "form-control"}),
                   'year': forms.Select(choices=YEAR_CHOICES, attrs={"class": "form-control"}),
                   'date': forms.SelectDateWidget(),

                   'desc': forms.Textarea(attrs={"class": "form-control"}), }
