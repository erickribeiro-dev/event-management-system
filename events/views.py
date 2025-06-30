from django.shortcuts import render
from django.views import generic
from .models import Event

# Create your views here.
def index(request):
    """A view representing the homepage."""
    return render(request, "events/index.html", {})

class EventListView(generic.ListView):
    """A view representing all the published events."""
    model = Event
    template_name = "events/event_list.html"
    context_object_name = "events"

    def get_queryset(self):
        # Only list published events, prefetching related tags for performance (Avoid N + 1 problem).
        # return Event.objects.filter(status="PUB").prefetch_related("tags")
        return Event.objects.all().prefetch_related("tags")

class EventDetailView(generic.DetailView):
    """A view representing details of a specific event."""
    model = Event
    template_name = "events/event_detail.html"
    context_object_name = "event"

    def get_queryset(self):
        # prefetch_related is not needed when displaying a single object.
        return Event.objects.filter(status="PUB")