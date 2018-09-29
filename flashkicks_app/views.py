from django.shortcuts import render, redirect
from .models import User
from django.contrib import messages

def index(request):
    return render(request, 'index.html')
    
def signupbtn(request):
    return redirect('/signup')

def loginbtn(request):
    return redirect('/login')

def signup_page(request):
    return render(request, 'signup_page.html')

def login_page(request):
    results = User.objects.login(request.POST)
    return render(request, 'login_page.html')

def signup(request):
    results = User.objects.signup(request.POST)
    if isinstance(results, User):
        request.session['user_id'] = results.id
        messages.add_message(request, messages.SUCCESS, 'Welcome, {}!'.format(results.username))
        return redirect('/dashboard')
    else:
        for key in results:
            messages.add_message(request, messages.ERROR, results[key])
        return redirect('/signup_page')

def login(request):
    results = User.objects.signup(request.POST)
    if isinstance(results, User):
        request.session['user_id'] = results.id
        messages.add_message(request, messages.SUCCESS, 'Welcome Back, {}!'.format(results.username))
        return redirect('/dashboard')
    else:
        for key in results:
            messages.add_message(request, messages.ERROR, results[key])
        return redirect('/login_page')






