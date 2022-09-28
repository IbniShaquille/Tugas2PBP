from email import contentmanager
from msilib.schema import CreateFolder
from django.shortcuts import render
from todolist.models import task
from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
from todolist.forms import CreateTaskForm
# Create your views here.
@login_required(login_url='/todolist/login/')
def show_todolist(request):
    data_tugas = task.objects.all()
    context = {
        'task': data_tugas,
        'nama': 'Ibni Shaquille Syauqi Ibrahim',
        'studentId': '2106706735'
    }
    return render(request, "todolist.html", context)

def show_xml(request):
    data = task.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = task.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = task.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = task.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('todolist:login')
    
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user) # melakukan login terlebih dahulu
            response = HttpResponseRedirect(reverse("todolist:show_todolist")) # membuat response
            response.set_cookie('last_login', str(datetime.datetime.now())) # membuat cookie last_login dan menambahkannya ke dalam response
            return response
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('todolist:login'))
    response.delete_cookie('last_login')
    return redirect('todolist:login')

def create(request):
    createForm = CreateTaskForm(request.POST or None)
    if request.method == 'POST':
        createForm = CreateTaskForm(request.POST)
        if createForm.is_valid():
            createForm.instance.user = request.user
            createForm.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('todolist:show_todolist')
    context={
        'page_title':'tambah tugas',
        'createForm':createForm,
        }
    return render(request, 'create-task.html', context)
