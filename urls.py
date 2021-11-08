from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('login/', views.user_login, name='login'),
    path('singup/', views.user_singup, name='singup'),
    path('logout/', views.user_logout, name='logout'),
    path('addquiz/', views.add_quiz, name='addquiz'),
    path('addannouncement/', views.add_anc, name='addannouncement'),
    path('updatequiz/<int:id>/', views.update_quiz, name='updatequiz'),
    path('deletequiz/<int:id>/', views.delete_quiz, name='delete'),


]
