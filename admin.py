# Register your models here
from django.contrib import admin
from .models import quiz, Profile, Announcement, Question, Choice,Vote
# Register your models here.


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 4


class QuestionAdmin(admin.ModelAdmin):
    fieids = {'question_text', 'start_time', 'end_time',
              'branch', 'year', 'total_votes', 'posted_by'}
    inlines = [ChoiceInline]


admin.site.register(Profile)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Vote)

admin.site.register(Choice)
admin.site.register(quiz)
admin.site.register(Announcement)
