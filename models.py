# Create your models here
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.deletion import CASCADE

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

)
BRANCH_CHOICES2 = (
    ("cse", "CSE"),
    ("eee", "EEE"),
    ("ece", "ECE"),
    ("mec", "MECHANICAL"),
    ("civ", "CIVIL"),
    ("bce", "BIOTECH"),
    ("phe", "PHARMA"),
    ("mat", "MNC"),
    ("ALL", "ALL"),
)
YEAR_CHOICES = []
for i in range(15, 30):
    YEAR_CHOICES.append((str(i), str(i)))
YEAR_CHOICES.append((str(0), str(0)))


class User(AbstractUser):
    is_student = models.BooleanField('Is student', default=True)
    is_professor = models.BooleanField('Is professor', default=False)
    branch = models.CharField(
        max_length=20, choices=BRANCH_CHOICES, default=False)
    year = models.CharField(max_length=5, choices=YEAR_CHOICES, default=False)
    RollNo = models.IntegerField(
        default=False, unique=True)

# Create your models here.


class quiz(models.Model):

    posted_by = models.ForeignKey(User, on_delete=CASCADE)
    subcode = models.CharField(max_length=15)
    branch = models.CharField(max_length=20, choices=BRANCH_CHOICES)
    year = models.CharField(max_length=10, choices=YEAR_CHOICES)
    date_posted = models.DateField()
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    quizurl = models.URLField()
    desc = models.TextField()


class Announcement(models.Model):

    posted_by = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    subcode = models.CharField(max_length=15)
    branch = models.CharField(max_length=20, choices=BRANCH_CHOICES2)
    year = models.CharField(max_length=10, choices=YEAR_CHOICES)
    date = models.DateTimeField()
    desc = models.TextField()
