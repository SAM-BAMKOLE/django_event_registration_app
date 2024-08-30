from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user
from django.http import HttpRequest
from .models import Event
from .forms import EventForm

# Create your views here.
@login_required
def create_new_event(request: HttpRequest):
    form = EventForm()

    if request.method == "POST":
        user = get_user(request)
        form = EventForm(request.POST)

        if form.is_valid():
            event = form.save(commit=False)  # Don't save to the database yet
            event.organizer = request.user  # Set the organizer to the current user
            event.save()  # Save the instance to the database

            return redirect('home_page')
    
    return render(request, "create.html", { "form": form })

def event_view(request: HttpRequest, slug):
    event = get_object_or_404(Event, slug=slug)

    return render(request, "view.html", { "event": event })

@login_required
def event_edit(request: HttpRequest, slug):
    event = get_object_or_404(Event, slug=slug)
    user = get_user(request)

    if event.organizer != user:
        return redirect('view_event', slug=slug)

    form = EventForm(instance=event)

    if request.method == "POST":
        form = EventForm(request.POST, instance=event)

        if form.is_valid():
            form.save()
            return redirect("home_page")    
    return render(request, "edit.html", { "event": event, "form": form })

# @login_required
# def edit_event(request: HttpRequest):
