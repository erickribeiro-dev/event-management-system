from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.utils import timezone
from django.views import generic
from .forms import EventForm
from .models import Event
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView

# Create your views here.
def index(request):
    """Represents the homepage."""
    return render(request, "events/index.html", {})

class EventListView(generic.ListView):
    """Represents all the published events."""
    model = Event
    template_name = "events/event_list.html"
    context_object_name = "events"

    def get_queryset(self):
        # Only query events that have been published and whose start_datetime is in the future.
        # Only list published events, prefetching related tags for performance (Avoid N + 1 problem).
        return Event.objects.filter(
            status="PUB",
            start_datetime__gte=timezone.now()
        ).prefetch_related("tags")

class EventDetailView(generic.DetailView):
    """Represents details of a specific event."""
    model = Event
    template_name = "events/event_detail.html"
    context_object_name = "event"

    def get_queryset(self):
        # Only display published events and events whose start_datetime is in the future.
        # prefetch_related is not needed when displaying a single object.
        return Event.objects.filter(
            status="PUB",
            start_datetime__gte=timezone.now()
        )
    
# Event CRUD
# class EventCreateView(LoginRequiredMixin, CreateView):
#     pass

@login_required
def create_event(request):
    """Creates a new event."""
    # If the user submits the event creation form (POST), process it and save to the database.
    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            # Create an event instance, but don't save to the database yet.
            event_instance = form.save(commit=False)
            # Assign the current user as the event organizer.
            event_instance.organizer = request.user
            # Save the event instance to the database.
            # This makes the event_instance object accessible for Many-to-many relationships.
            event_instance.save()
            # Save the Many-to-Many data *after* the instance has a primary key.
            form.save_m2m()
            return redirect("events:index")
    # If the user requests the event creation form (GET), display the empty form.
    else:
        form = EventForm()
    context = {"form": form}
    return render(request, "events/event_form.html", context)

# class EventUpdateView(LoginRequiredMixin, UpdateView):
#     pass

# def update_event(request):
#     pass
