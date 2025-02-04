from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path("", register, name='register'),
    path("login/", login_user, name='login'),
    path("list", task_list, name='task_list'),
    path("create/", create_task, name='create_task'),
    path("update/<int:id>", update, name='update'),
    path("delete/<int:id>", delete, name='delete'),
    path("logout/", logout_user, name='logout'),
    path("user/", user_detail, name='user_detail'),
]