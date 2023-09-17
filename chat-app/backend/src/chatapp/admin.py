from django.contrib import admin
from .models import Profile, ChatMessage

class ProfileAdmin(admin.ModelAdmin):
    list_editable=["verified"]
    list_display=["user", "full_name", "verified"]

class ChatMessageAdmin(admin.ModelAdmin):
    list_editable=["is_read"]
    list_display=["sender", "receiver", "message", "is_read"]


admin.site.register(Profile, ProfileAdmin)
admin.site.register(ChatMessage, ChatMessageAdmin)
