from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if request.user.is_superuser:
            login(request, user)
            return redirect('home')
        elif not request.user.is_superuser:
            login(request,user)
            return redirect('home')
        else:
            messages.success(request, "There was an error, try again")
            return redirect('login')
    else:
        return render(request, 'authenticate/login.html', {})

def logout_user(request):
    logout(request)
    messages.success(request,'You were Logged out!')
    return redirect('home')


def register_user(request):
    return render(request, 'authenticate/register_user.html', {})