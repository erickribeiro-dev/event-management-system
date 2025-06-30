from django.urls import path
from . import views

app_name = "events"
urlpatterns = [
    path("", views.index, name="index"),
    path("events/", views.EventListView.as_view(), name="event_list"),
    # TODO: Change event detail path to a slug
    path("events/<int:pk>", views.EventDetailView.as_view(), name="event_detail"),
]