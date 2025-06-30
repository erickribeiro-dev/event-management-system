from django.db import models

# Create your models here.
class Category(models.Model):
    # Categories can't have the same name.
    name = models.CharField(max_length=255, unique=True)
    
    def __str__(self):
        return self.name
    
class Tag(models.Model):
    name = models.CharField(max_length=255, unique=True)
    
    def __str__(self):
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
    # slug = models.SlugField(unique=True, max_length=255, blank=True)

    # Date & Time
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

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

    # TODO: implement Organizer
    # organizer = models.ForeignKey(User, on_delete=models.CASCADE)

    # Auditing fields
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        """String representation for the Event model."""
        return self.title
    
    class Meta:
        # Newly created events come first
        ordering = ["-created_at", "start_time"]