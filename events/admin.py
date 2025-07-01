from django.contrib import admin
from .models import Category, Tag, Event

# Register your models here.
class EventAdmin(admin.ModelAdmin):
    list_display = ("title", "slug",)
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(Category)
admin.site.register(Tag)
# admin.site.register(Event)
admin.site.register(Event, EventAdmin)