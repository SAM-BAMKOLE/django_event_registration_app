from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, get_user, logout
from .forms import RegisterForm
from  django.contrib.auth.models import AnonymousUser
from registrations.models import Registration
from django.contrib.auth.decorators import login_required

# Create your views here.
def register(request: HttpRequest):
    form = RegisterForm()

    user = get_user(request)

    if request.method == "POST":
        form = RegisterForm(request.POST)
        # validate form
        if form.is_valid():
            login(request, form.save())
            return redirect(to='home_page')
        
    if not isinstance(user, AnonymousUser):
        return redirect("home_page")
    
    return render(request, 'register.html', { "form": form, "user": user })


def login_view(request: HttpRequest):
    user = get_user(request)

    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        # validate form
        if form.is_valid():
            login(request, form.get_user())
            # redirect to
            if request.POST.get('next') or 'next' in request.POST:
                return redirect(request.POST.get('next'))
            return redirect('home_page')
        
    if not isinstance(user, AnonymousUser):
        return redirect("home_page")
    
    form = AuthenticationForm()
    return render(request, 'login.html', { "form": form, "user": user })


def logout_view(request):
    if request.method == 'POST':
        logout(request)
        
    return redirect(to="home_page")

@login_required
def registered_events(request: HttpRequest):
    registrations = Registration.objects.filter(user=request.user)
    return render(request, 'registered_events.html', { "registrations": registrations })