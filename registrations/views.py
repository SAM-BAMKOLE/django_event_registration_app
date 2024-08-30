from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpRequest
from django.contrib.auth.decorators import login_required
from events.models import Event
from .models import Registration

# Create your views here.
@login_required
def add_registration(request: HttpRequest, id):
    if request.method == "POST":
        user = request.user
        event = get_object_or_404(Event, pk=id)

        if event.organizer == user:
            return redirect('view_event', slug=event.slug)

        _ = Registration.objects.create(user=user, event=event)

        return redirect('home_page')
    
    return redirect('home_page')

