from django.contrib import admin
from .models import Entry


@admin.register(Entry)
class EntryAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "email", "paypal_email", "created_at")
    search_fields = ("first_name", "last_name", "email", "paypal_email", "postcode")
    list_filter = ("created_at",)
    readonly_fields = ("created_at",)
