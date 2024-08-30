from django.urls import path
from . import views

urlpatterns = [
    path("create/", views.create_new_event, name="create_event"),
    path("<slug:slug>/", views.event_view, name="view_event"),
    path("edit/<slug:slug>/", views.event_edit, name="edit_event"),
]