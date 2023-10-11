from django.contrib import admin

from .models import ContactModel


@admin.register(ContactModel)
class ContactAdmin(admin.ModelAdmin):
    fields = ('name', 'email', 'is_read_by_admin', 'message')
    list_display = ('name', 'email', 'is_read_by_admin')
    list_editable = ('is_read_by_admin',)
