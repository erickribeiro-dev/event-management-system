from django.urls import path
from . import views

app_name = "events"
urlpatterns = [
    path("", views.index, name="index"),
    path("events/", views.EventListView.as_view(), name="event_list"),
    path("events/<slug:slug>", views.EventDetailView.as_view(), name="event_detail"),
    path("events/create/", views.create_event, name="create_event"),
    path("events/update/<int:pk>", views.update_event, name="update_event"),
    path("events/delete/<int:pk>/", views.delete_event, name="delete_event"),
]