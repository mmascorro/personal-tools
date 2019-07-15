from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

def index(request):
    if request.user.is_authenticated:
        return render(request, 'core/index-user.html')
    else:
        return render(request, 'core/index.html')


def site_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('homepage')

        else:

            return render(request, 'core/login.html')
    else:
        return render(request, 'core/login.html')

def site_logout(request):
    logout(request)
    return redirect('homepage')
