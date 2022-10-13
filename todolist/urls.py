# TODO: Implement Routings Here

from django.urls import path
from todolist.views import show_todolist, register, login_user, logout_user, create, show_json, add

app_name = 'todolist'

urlpatterns = [
    path('', show_todolist, name='show_todolist'),
    path('create-task/', create, name='create'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('json/', show_json, name='show_json'),
    path('add/', add, name='add'),
]
