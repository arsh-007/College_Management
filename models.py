# Create your models here
from django.db import models
from django.db.models.deletion import CASCADE
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.
BRANCH_CHOICES = (
    ("cse", "CSE"),
    ("eee", "EEE"),
    ("ece", "ECE"),
    ("mec", "MECH"),
    ("civ", "CIVIL"),
    ("bce", "BIOTECH"),
    ("phe", "PHARMA"),
    ("mat", "MNC"),
    ("ALL", "ALL")
)
YEAR_CHOICES = []
for i in range(15, 30):
    YEAR_CHOICES.append((str(i), str(i)))
YEAR_CHOICES.append(("ALL", "ALL"))


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_student = models.BooleanField('Is student', default=True)
    is_professor = models.BooleanField('Is professor', default=False)

    def __str__(self):
        return f'{self.user.username} Profile'
# Create your models here.


class quiz(models.Model):

    posted_by = models.ForeignKey(User, on_delete=CASCADE)
    subcode = models.CharField(max_length=15)
    branch = models.CharField(max_length=20, choices=BRANCH_CHOICES)
    year = models.CharField(max_length=10, choices=YEAR_CHOICES)
    date_posted = models.DateTimeField(default=timezone.now)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    quizurl = models.URLField()
    desc = models.TextField()


class Announcement(models.Model):

    posted_by = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    subcode = models.CharField(max_length=15)
    branch = models.CharField(max_length=20, choices=BRANCH_CHOICES)
    year = models.CharField(max_length=10, choices=YEAR_CHOICES)
    date = models.DateTimeField(default=timezone.now)
    desc = models.TextField()
    # font color thoda change


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    start_date = models.DateTimeField('date published')
    end_date = models.DateTimeField('date ended')
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    branch = models.CharField(max_length=20, choices=BRANCH_CHOICES)
    year = models.CharField(max_length=10, choices=YEAR_CHOICES)
    pub_date = models.DateTimeField(default=timezone.now)
    total_votes = models.IntegerField(default=0)

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(
        Question, on_delete=models.CASCADE, related_name='choices')
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text


class Vote(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    voter = models.ForeignKey(User, on_delete=models.CASCADE)
