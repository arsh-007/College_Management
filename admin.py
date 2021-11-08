# Register your models here
from django.contrib import admin
from .models import quiz, User, Announcement
# Register your models here.


@admin.register(quiz)
class quizModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'subcode', 'branch', 'year',
                    'quizurl', 'date_posted', 'date', 'start_time', 'end_time', 'posted_by']


@admin.register(User)
class UserModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'username', 'password', 'email',
                    'branch', 'year', 'is_student', 'is_professor', 'RollNo']


@admin.register(Announcement)
class AnnouncementModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'subcode',
                    'branch', 'year', 'date', 'posted_by']
