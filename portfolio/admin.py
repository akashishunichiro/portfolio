from django.contrib import admin
from .models import Profile, Project, ContactMessage

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("full_name", "title", "email")
    readonly_fields = ()

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "demo_url", "repo_url", "order", "created_at")
    list_editable = ("order",)

@admin.register(ContactMessage)
class ContactAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "phone", "created_at", "read")
    list_filter = ("read", "created_at")
    actions = ["mark_as_read"]

    def mark_as_read(self, request, queryset):
        queryset.update(read=True)
    mark_as_read.short_description = "Mark selected messages as read"
