from django.http import HttpRequest
from django.shortcuts import render
from events.models import Event
from registrations.models import Registration
from django.contrib.auth.models import AbstractUser

def homepage(request: HttpRequest):
    events = Event.objects.all().order_by("-created_at")
    if isinstance(request.user, AbstractUser):
        user_registrations = Registration.objects.filter(user=request.user).values_list('id', flat=True)
        return render(request, 'home.html', { "events": events, 'user_registrations': user_registrations })

    # event_id = user_registrations.event.
    return render(request, 'home.html', { "events": events })