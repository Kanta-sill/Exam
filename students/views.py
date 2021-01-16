from django.shortcuts import render, redirect
from .models import Student
from .forms import LoginForm
from django.contrib import messages

# Create your views here.

def login(request):
    if request.method=='POST':
        form=LoginForm(request.POST)
        if form.is_valid():
            stu=Student.objects.all()
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            if (username==i.username for i in  stu) or (password==i.password for i in stu):
                request.session['user']=username
                request.session['pass']=password
                return redirect('indexSt')
    else:
        form=LoginForm()
    return render(request, 'student/login.html', {'form':form})

def logout(request):
    del request.session['user']
    del request.session['pass']
    return render(request, 'student/logout.html')

def checklogin(request):
    if (request.session.get('user')==None or request.session.get('pass') == None):
        messages.success(request, f'You must login first')
        return redirect('loginSt')

def index(request):
    if (request.session.get('user')==None or request.session.get('pass') == None):
        # messages.success(request, f'You must login first')
        return redirect('loginSt')
    else:
        return render(request, 'student/index.html')