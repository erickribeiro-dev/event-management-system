from django.urls import path
from . import views

app_name = "events"
urlpatterns = [
    path("", views.index, name="index"),
    path("events/", views.EventListView.as_view(), name="event_list"),
    path("events/<slug:slug>", views.EventDetailView.as_view(), name="event_detail"),
]