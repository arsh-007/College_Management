# Generated by Django 3.2.5 on 2021-11-13 16:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.CharField(max_length=200)),
                ('start_date', models.DateTimeField(verbose_name='date published')),
                ('end_date', models.DateTimeField(verbose_name='date ended')),
                ('title', models.CharField(max_length=100)),
                ('branch', models.CharField(choices=[('cse', 'CSE'), ('eee', 'EEE'), ('ece', 'ECE'), ('mec', 'MECH'), ('civ', 'CIVIL'), ('bce', 'BIOTECH'), ('phe', 'PHARMA'), ('mat', 'MNC'), ('ALL', 'ALL')], max_length=20)),
                ('year', models.CharField(choices=[('15', '15'), ('16', '16'), ('17', '17'), ('18', '18'), ('19', '19'), ('20', '20'), ('21', '21'), ('22', '22'), ('23', '23'), ('24', '24'), ('25', '25'), ('26', '26'), ('27', '27'), ('28', '28'), ('29', '29'), ('ALL', 'ALL')], max_length=10)),
                ('pub_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('posted_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.question')),
                ('voter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='quiz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subcode', models.CharField(max_length=15)),
                ('branch', models.CharField(choices=[('cse', 'CSE'), ('eee', 'EEE'), ('ece', 'ECE'), ('mec', 'MECH'), ('civ', 'CIVIL'), ('bce', 'BIOTECH'), ('phe', 'PHARMA'), ('mat', 'MNC'), ('ALL', 'ALL')], max_length=20)),
                ('year', models.CharField(choices=[('15', '15'), ('16', '16'), ('17', '17'), ('18', '18'), ('19', '19'), ('20', '20'), ('21', '21'), ('22', '22'), ('23', '23'), ('24', '24'), ('25', '25'), ('26', '26'), ('27', '27'), ('28', '28'), ('29', '29'), ('ALL', 'ALL')], max_length=10)),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('quizurl', models.URLField()),
                ('desc', models.TextField()),
                ('posted_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_student', models.BooleanField(default=True, verbose_name='Is student')),
                ('is_professor', models.BooleanField(default=False, verbose_name='Is professor')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice_text', models.CharField(max_length=200)),
                ('votes', models.IntegerField(default=0)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='choices', to='main.question')),
            ],
        ),
        migrations.CreateModel(
            name='Announcement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('subcode', models.CharField(max_length=15)),
                ('branch', models.CharField(choices=[('cse', 'CSE'), ('eee', 'EEE'), ('ece', 'ECE'), ('mec', 'MECH'), ('civ', 'CIVIL'), ('bce', 'BIOTECH'), ('phe', 'PHARMA'), ('mat', 'MNC'), ('ALL', 'ALL')], max_length=20)),
                ('year', models.CharField(choices=[('15', '15'), ('16', '16'), ('17', '17'), ('18', '18'), ('19', '19'), ('20', '20'), ('21', '21'), ('22', '22'), ('23', '23'), ('24', '24'), ('25', '25'), ('26', '26'), ('27', '27'), ('28', '28'), ('29', '29'), ('ALL', 'ALL')], max_length=10)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('desc', models.TextField()),
                ('posted_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
