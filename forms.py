from django.db.models.fields import DateField, DateTimeField
from django.forms import widgets, ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField

from django.utils.regex_helper import Choice
from .models import Announcement, Question, User, quiz, Choice
from . models import BRANCH_CHOICES, YEAR_CHOICES
from django.contrib.admin import widgets
import datetime
from django.core.validators import EmailValidator
from django.utils.deconstruct import deconstructible


@deconstructible
class WhitelistEmailValidator(EmailValidator):

    def validate_domain_part(self, domain_part):
        return False

    def __eq__(self, other):
        return isinstance(other, WhitelistEmailValidator) and super().__eq__(other)


class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(
        attrs={'autofocus': True, 'class': 'form-control'}))
    password = forms.CharField(label='password', strip=False, widget=forms.PasswordInput(
        attrs={'autocomplete': True, 'class': 'form-control'}))


class SingUpForm(UserCreationForm):
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control"}))
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control"}))

    username = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control"}))
    password1 = forms.CharField(label='Password',
                                widget=forms.PasswordInput(attrs={"class": "form-control"}))
    password2 = forms.CharField(label='Confirm Password',
                                widget=forms.PasswordInput(attrs={"class": "form-control"}))
    email = forms.EmailField(validators=[WhitelistEmailValidator(whitelist=['itbhu.ac.in'])], label='Institute Email id',
                             widget=forms.EmailInput(attrs={'class': 'form-control'}))

    def clean_email(self):
        data = self.cleaned_data['email']
        if User.objects.filter(email=data).exists():
            raise forms.ValidationError("This email is already in use")
        return data

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1',
                  'password2']
        labels = {'password2': 'Confirm Password',
                  'password1': 'Password', 'email': 'Institute mail id'}


class QuizForm (forms.ModelForm):
    class Meta:
        model = quiz
        fields = ['subcode', 'branch', 'year',
                  'start_time', 'end_time', 'quizurl', 'desc']
        labels = {'subcode': 'Subject code', 'branch': 'Branch', 'year': 'Year',
                  'quizurl': 'Link', 'start_time': 'Starting Time Format(YYYY-MM-DD HH:MM:SS)', 'end_time': 'Ending Time Format(YYYY-MM-DD HH:MM:SS)', 'desc': 'Description'}
        widgets = {'subcode': forms.TextInput(attrs={"class": "form-control"}),
                   'branch': forms.Select(choices=BRANCH_CHOICES, attrs={"class": "form-control"}),
                   'year': forms.Select(choices=YEAR_CHOICES, attrs={"class": "form-control"}),
                   'start_time': forms.DateTimeInput(format='%Y-%m-%d %H:%M:%S'),
                   'end_time': forms.DateTimeInput(format='%Y-%m-%d %H:%M:%S'),
                   'quizurl': forms.URLInput(attrs={"class": "form-control"}),
                   'desc': forms.Textarea(attrs={"class": "form-control"}), }


class Ancform (forms.ModelForm):
    class Meta:
        model = Announcement
        fields = ['title', 'subcode', 'branch', 'year',  'desc']
        labels = {'title': 'Title', 'subcode': 'Subject code',
                  'branch': 'Branch', 'year': 'Year',  'desc': 'Description'}
        widgets = {'title': forms.TextInput(attrs={"class": "form-control"}),
                   'subcode': forms.TextInput(attrs={"class": "form-control"}),
                   'branch': forms.Select(choices=BRANCH_CHOICES, attrs={"class": "form-control"}),
                   'year': forms.Select(choices=YEAR_CHOICES, attrs={"class": "form-control"}),
                   'desc': forms.Textarea(attrs={"class": "form-control"}), }


class PollQuestion(forms.ModelForm):

    choice1 = forms.CharField(label='Choice 1', max_length=100, min_length=2,
                              widget=forms.TextInput(attrs={'class': 'form-control'}))
    choice2 = forms.CharField(label='Choice 2', max_length=100, min_length=2,
                              widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Question
        fields = ['question_text', 'branch', 'year',
                  'title', 'start_date', 'end_date', 'choice1', 'choice2']
        widgets = {'title': forms.TextInput(attrs={"class": "form-control"}),
                   'question_text': forms.TextInput(attrs={"class": "form-control"}),
                   'branch': forms.Select(choices=BRANCH_CHOICES, attrs={"class": "form-control"}),
                   'year': forms.Select(choices=YEAR_CHOICES, attrs={"class": "form-control"}),
                   'start_date': forms.DateInput(attrs={"class": "form-control"}),
                   'end_date': forms.DateInput(attrs={"class": "form-control"}), }


class Addchoices(forms.ModelForm):
    class Meta:
        model = Choice

        fields = ['choice_text']
        widgets = {'choice_text': forms.TextInput(
            attrs={"class": "form-control"}), }