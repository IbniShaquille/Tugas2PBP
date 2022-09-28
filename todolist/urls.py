# TODO: Implement Routings Here

from django.urls import path
from todolist.views import show_todolist, show_json, show_json_by_id, show_xml, show_xml_by_id, register, login_user, logout_user, create

app_name = 'todolist'

urlpatterns = [
    path('html/', show_todolist, name='show_todolist'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<int:id>', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>', show_json_by_id, name='show_json_by_id'),
    path('create-task/', create, name='create'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
]
