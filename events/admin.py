from django.contrib import admin
from .models import Category, Tag, Event

# Register your models here.
# ModelAdmin for Event
class EventAdmin(admin.ModelAdmin):
    list_display = ("title", "created_at", "updated_at", "is_past", "is_ongoing", "is_upcoming")
    list_filter = ("category", "tags", "status")
    search_fields = ("title", "description", "category__name", "tags__name")
    prepopulated_fields = {"slug": ("title",)}

# ModelAdmin for Category
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)

# ModelAdmin for Tag
class TagAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)

admin.site.register(Event, EventAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)