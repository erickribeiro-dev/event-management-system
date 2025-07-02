from django import forms
from .models import Event

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = "__all__"
        exclude = ["slug", "organizer"]
        # Add Bootstrap classes to the fields.
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter event title..."}),
            "description": forms.Textarea(attrs={"class": "form-control", "placeholder": "Enter description...", "rows": 3}), # Rows for textarea
            
            "location": forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter location..."}),
            "start_datetime": forms.DateTimeInput(attrs={"class": "form-control", "type": "datetime-local"}), # Datetime input
            "end_datetime": forms.DateTimeInput(attrs={"class": "form-control", "type": "datetime-local"}), # Datetime input
            
            "currency": forms.Select(attrs={"class": "form-select"}),
            "price": forms.NumberInput(attrs={"class": "form-control", "step": "0.01"}), # Decimal prices
            
            "capacity": forms.NumberInput(attrs={"class": "form-control", "step": "1"}),
            "category": forms.Select(attrs={"class": "form-select"}),
            "tags": forms.SelectMultiple(attrs={"class": "form-select"}), # Multiple selection
            "is_featured": forms.CheckboxInput(attrs={"class": "form-check-input"}),
            "featured_text": forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter featured text..."}),
        }