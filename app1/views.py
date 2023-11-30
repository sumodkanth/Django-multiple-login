from django.shortcuts import render
from app1.models import Customuser

from django.contrib.auth import login, authenticate, logout
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request, 'home.html')


def adminsignup(request):
    if request.method == "POST":
        u = request.POST['u']
        v = request.POST['v']
        w = request.POST['w']
        x = request.POST['x']
        y = request.POST['y']

        a = request.POST['a']

        f = Customuser.objects.create_user(username=u, first_name=v, last_name=w, email=x, password=y,
                                           phone=a)
        f.is_admin = True
        f.save()
        return home(request)

    return render(request, 'adminsignup.html')


def studentsignup(request):
    if request.method == "POST":
        u = request.POST['u']
        v = request.POST['v']
        w = request.POST['w']
        x = request.POST['x']
        y = request.POST['y']

        a = request.POST['a']

        f = Customuser.objects.create_user(username=u, first_name=v, last_name=w, email=x, password=y,
                                           phone=a)
        f.is_student = True
        f.save()
        return home(request)
    return render(request, 'studentsignup.html')


def teachersignup(request):
    if request.method == "POST":
        u = request.POST['u']
        v = request.POST['v']
        w = request.POST['w']
        x = request.POST['x']
        y = request.POST['y']

        a = request.POST['a']

        f = Customuser.objects.create_user(username=u, first_name=v, last_name=w, email=x, password=y,
                                           phone=a)
        f.is_teacher = True
        f.save()
        return home(request)
    return render(request, 'teachersignup.html')


def user_login(request):
    if request.method == "POST":
        u = request.POST['u']
        y = request.POST['y']
        user = authenticate(username=u, password=y)
        if user and user.is_admin == True:
            return render(request, 'adminhome.html')
        elif user and user.is_student == True:
            return render(request, 'studenthome.html')
        elif user and user.is_teacher == True:
            return render(request, 'teacherhome.html')
        else:
            messages.error(request,"Invalid credential")
    return render(request, 'login.html')


def user_logout(request):
    logout(request)
    return render(request, 'logout.html')
