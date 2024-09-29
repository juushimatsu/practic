from django.shortcuts import render, redirect
from django.http import HttpRequest
from .forms import RegisterForm
from django.contrib.auth import login
from .forms import LoginForm
from .models import Profile
from .forms import ProfileForm
from django.contrib.auth.decorators import login_required

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()  # Сохраняем пользователя в базе данных
            return redirect('home')  # Перенаправляем на главную страницу после успешной регистрации
    else:
        form = RegisterForm()
    
    return render(request, 'account/register.html', {'form': form})

def login_user(request: HttpRequest):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            if user is not None:
                login(request, user)
                return redirect('home')  # Перенаправляем на главную страницу после успешной авторизации
        else:
            form = LoginForm(request=request)
    else:
        form = LoginForm()

    return render(request, 'account/login.html', context={
        'title': 'Авторизация',
        'form': form,
    })

from django.contrib.auth import logout

def logout_user(request):
    logout(request)
    return redirect('home')

@login_required
def profile_view(request):
    try:
        user_profile = Profile.objects.get(user=request.user)
        print("Профиль найден:", user_profile)
        return render(request, 'account/profile.html', {'user': user_profile})
    except Profile.DoesNotExist:
        print("Профиль не найден для пользователя:", request.user)
        return redirect('registration')

@login_required(login_url='login')
def delete_profile(request):
    user_profile = Profile.objects.get(user=request.user)  # Получаем профиль пользователя
    user = request.user  # Получаем текущего пользователя

    user_profile.delete()  # Удаляем профиль
    user.delete()  # Удаляем пользователя
    logout(request)
    return redirect('home')

@login_required(login_url='login')
def profile_edit_view(request):
    profile = Profile.objects.get(user=request.user)
    
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')  # или на нужную вам страницу
    else:
        form = ProfileForm(instance=profile)
    
    return render(request, 'account/profile_edit.html', {'form': form})
