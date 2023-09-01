# app_name/views.py

from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect,get_object_or_404
from django.shortcuts import render
from .models import Statistic
from .forms import StatisticForm 

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            # Handle invalid login
            pass
    return render(request, 'login.html')

def registration_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration.html', {'form': form})


def dashboard(request):
    statistics = Statistic.objects.all()
    return render(request, 'dashboard.html', {'statistics': statistics})
    

def add_statistic(request):
    if request.method == 'POST':
        form = StatisticForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = StatisticForm()
    return render(request, 'add_statistic.html', {'form': form})

def edit_statistic(request, statistic_id):
    statistic = get_object_or_404(Statistic, pk=statistic_id)
    if request.method == 'POST':
        form = StatisticForm(request.POST, instance=statistic)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = StatisticForm(instance=statistic)
    return render(request, 'edit_statistic.html', {'form': form})

def delete_statistic(request, statistic_id):
    statistic = get_object_or_404(Statistic, pk=statistic_id)
    if request.method == 'POST':
        statistic.delete()
        return redirect('dashboard')
    return render(request, 'delete_statistic.html', {'statistic': statistic})