from django.contrib import admin
from .models import Event, Registration, Institute
from import_export.admin import ImportExportModelAdmin, ImportExportActionModelAdmin

admin.site.site_header = 'Career And Counseling Cell'

# Register your models here.


class InlineRegistration(admin.TabularInline):
    model = Registration


class EventAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
    inlines = [InlineRegistration]
    list_display = ('event_name', 'description', 'date', 'status',)
    list_display_links = ('event_name', 'description')
    list_editable = ('status', 'date')
    list_filter = ('date', 'status')
    search_fields = ('user', 'roll_no', 'course', 'branch')
    list_max_show_all = 50


class RegistrationAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
    list_display = ('user', 'event', 'date', 'attended')
    list_display_links = ('user', 'event')
    list_editable = ('attended',)
    list_filter = ('date', 'event', 'attended')
    search_fields = ('user', 'event')


class InstitutesAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
    list_display = ('institute', 'contact_person', 'contact_person_phone_number', 'email')
    list_display_links = ('institute', 'contact_person', 'contact_person_phone_number', 'email')
    list_filter = ('institute',)
    search_fields = ('institute', 'contact_person', 'contact_person_phone_number', 'email', 'previous_events')


admin.site.register(Event, EventAdmin)
admin.site.register(Registration, RegistrationAdmin)
admin.site.register(Institute, InstitutesAdmin)
