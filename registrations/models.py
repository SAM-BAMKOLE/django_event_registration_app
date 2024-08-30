from django.db import models
from django.contrib.auth.models import User
# from event_registration.events.models import Event
from events.models import Event

# Create your models here.
class Registration(models.Model):
    user                                  = models.ForeignKey(User, on_delete=models.CASCADE)
    event                               = models.ForeignKey(Event, on_delete=models.RESTRICT)
    registration_date       = models.DateTimeField(auto_now_add=True)
    payment_status          = models.BooleanField(default=False)


    def __str__(self):
        return f'Registration >> user->{self.user.username} event->{self.event.title}'