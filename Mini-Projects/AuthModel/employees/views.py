from django.shortcuts import render
from django.http import HttpResponse
from .forms import EmployeeForms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout, login
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required


# Create your views here.

def register_view(request):
    if request.method == 'POST':
        form = EmployeeForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else: 

        form = EmployeeForms()
    
    return render (request, 'employees/index.html',{"form":form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            user=form.get_user()
            login(request,user)
            return redirect('dashboard')
    else:
        form = AuthenticationForm()
    
    return render (request,'employees/login.html',{'form':form})

@login_required
def dashboard_view(request):
    employee = request.user.employee
    return render(request,'employees/dashboard.html',{'employee':employee})

def logout_view(request):
    logout(request)
    return redirect('login')