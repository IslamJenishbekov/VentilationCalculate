from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import SignUpForm


def home(request):
    """Главная страница."""
    return render(request, 'projects/projects_list.html')


def signup(request):
    """Представление для регистрации нового пользователя."""
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Автоматический вход после регистрации
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})
