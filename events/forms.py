from django import forms
from .models import Event

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'description', 'date', 'location', 'category', 'max_participants']
        widgets = {
            'date': forms.DateTimeInput(attrs={
                'type': 'datetime-local',
                #'format': '%Y-%m-%dT%H:%M',  # Only needed if you need to customize the layout in html
            }),
        }

    # def __init__(self, *args, **kwargs): #only needed if you need to customize the layout in html
    #     super().__init__(*args, **kwargs)
    #     self.fields['date'].input_formats = ['%Y-%m-%dT%H:%M']
