from django.contrib import admin
from django.db import models
from django.utils import timezone
from django.utils.text import slugify

# Create your models here.
class Category(models.Model):
    """Represents a category related to an event."""
    # Categories can't have the same name.
    name = models.CharField(max_length=255, unique=True)
    
    def __str__(self):
        """String representation for the Category model."""
        return self.name
    
    class Meta:
        verbose_name_plural = "Categories"
    
class Tag(models.Model):
    """Represents tags related to an event."""
    # Tags can't have the same name.
    name = models.CharField(max_length=255, unique=True)
    
    def __str__(self):
        """String representation for the Tag model."""
        return self.name

class Event(models.Model):
    """Represents an event that users can attend."""
    STATUS_CHOICES = [
        ("DRA", "Draft"),
        ("PUB", "Published"),
        ("CAN", "Cancelled"),
        ("COM", "Completed"),
    ]
    CURRENCY_CHOICES = [
        ('BRL', 'R$'),
        ('USD', '$'),
        ('EUR', '€'),
        ('GBP', '£'),
        # Add more currencies as needed
    ]
    # Basic information
    title = models.CharField(max_length=255)
    description = models.TextField()
    # TODO: Move location to its own model and use ForeignKey here instead.
    # If reusability is needed or it becomes too complex, move it to a separate App
    location = models.CharField(max_length=255) # TODO: 
    # location = models.ForeignKey(Location, on_delete=models.SET_NULL)

    # TODO: implement Image & slug
    # Will be uploaded to MEDIA_ROOT + path
    # image = models.ImageField(upload_to="events/", blank=True, null=True)
    # Will be automatically generated. blank=True makes the field optional in forms.
    slug = models.SlugField(unique=True, max_length=255, blank=True, null=False)

    # Date & Time
    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField(null=True, blank=True) # Optional

    # Pricing & Capacity
    # Price example: 19.50
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    currency = models.CharField(max_length=3, choices=CURRENCY_CHOICES, default="BRL")
    capacity = models.PositiveIntegerField(null=True, blank=True, help_text="Leave empty for unlimited.")

    # Category, Tags, Status & Featured
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.SET_NULL)
    # Tags are not required in forms
    tags = models.ManyToManyField(Tag, blank=True)
    status = models.CharField(max_length=3, choices=STATUS_CHOICES, default="DRA")
    is_featured = models.BooleanField(default=False, help_text="Feature this event on the homepage.")
    featured_text = models.CharField(
        max_length=20,
        blank=True,    # Allow it to be empty in forms
        null=True,     # Allow it to be NULL in the database
        help_text="Custom text to display on the featured badge ('Hot!', 'New!', 'Limited Spots!'). Only visible if Is featured is checked."
    )

    # TODO: implement Organizer
    # organizer = models.ForeignKey(User, on_delete=models.CASCADE)

    # Auditing fields
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        """String representation for the Event model."""
        return self.title
    
    def save(self, *args, **kwargs):
        """Override the save method to generate a slug automatically based on event.title.
        Slugs with the same title will have a number appended to differentiate them.
        """
        if not self.slug:
            base_slug = slugify(self.title)
            unique_slug = base_slug
            num = 1
            # Append a number if the slug is not unique
            while Event.objects.filter(slug=unique_slug).exists():
                unique_slug = f"{base_slug}-{num}"
                num += 1
                
            self.slug = unique_slug
        super().save(*args, **kwargs)

    @admin.display(boolean=True, description="Ended")
    def is_past(self):
        """Check if an event is in the past."""
        now = timezone.now()
        # If the event has an end_datetime, return True if we're past the end time.
        if self.end_datetime:
            return self.end_datetime < now
        # Otherwise, return True if we're past the start_datetime.
        return self.start_datetime < now
        
    @admin.display(boolean=True, description="Ongoing")
    def is_ongoing(self):
        """Check if an event is ongoing."""
        now = timezone.now()
        # An event is ongoing if it has an end_datetime and if we're between its start and end datetimes.
        if self.end_datetime:
            return self.start_datetime <= now < self.end_datetime
        return False
    
    @admin.display(boolean=True, description="Upcoming")
    def is_upcoming(self):
        """Check if an event is upcoming."""
        now = timezone.now()
        # An event is upcoming if its start_datetime is in the future.
        return self.start_datetime > now

    class Meta:
        # Newly created events come first.
        ordering = ["-is_featured", "-created_at", "start_datetime"]