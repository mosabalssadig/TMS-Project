from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
#from requests import session
from .models import *
from datetime import datetime
from django.contrib.auth import authenticate, login

# Create your views here.


@login_required(login_url='signin')
def index(request):

    return render(request, "index.html", {
        'tasks': task.objects.all(),

    })



@login_required(login_url='signin')
def addUser(request):
    if request.method == "POST":
        fullname = request.POST.get("fullName")
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")

        if user.objects.filter(username=username).exists():
            print("Username already exists")
            return redirect('index')

        if user.objects.filter(email=email).exists():
            print("email already exists")
            return redirect('index')
        else:
            userSignUp = user.objects.create_user(
                fullname=fullname, username=username, email=email, password=password, is_staff=False)
            userSignUp.save()

            atuser = user.objects.get(username=username)
            attend = attendance_info.objects.create(
                userAtendance=atuser,
                in_time=datetime.now(),
            )

            attend.save()

            new = attendance_info.objects.get(
                userAtendance=atuser,)
            atuser.att = new
            atuser.save(update_fields=['att'])

            print("user was added successfully")
            return redirect('index')

    else:
        return render(request, "adduser.html")


@login_required(login_url='signin')
def attendance(request):

    users = user.objects.all()
    attend = attendance_info.objects.all()
    return render(request, "attendance.html", {
        "users": users,
        'attends': attend,
    })


@login_required(login_url='signin')
def addTask(request):

    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")
        start_time = request.POST.get("start_time")
        end_time = request.POST.get("end_time")
        user_id = user.objects.get(id=request.POST.get("taskuser"))
        addtask = task.objects.create(
            title=title, description=description, start_time=start_time, end_time=end_time, user_id=user_id)
        addtask.save()
        print("task was added successfully")
        return redirect('index')

    else:

        users = user.objects.all()
        return render(request, "addtask.html", {
            "users": users,
        })


def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        userSignin = authenticate(request,
                                  username=username, password=password)

        if userSignin is None:
            print('Wrong Username or Password')
            return redirect('signin')

        login(request, userSignin)
        print('Sign in successfully')
        print(f'{request.user.username}')
        return redirect('/')
    else:
        return render(request, 'signin.html')


@login_required(login_url='signin')
def signout(request):
    auth.logout(request)
    return redirect('signin')


@login_required(login_url='signin')
def deleteuser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        user.objects.filter(username=username).delete()
        return redirect('attendance')
