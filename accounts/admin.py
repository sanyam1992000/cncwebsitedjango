from django.contrib import admin
from .models import UserProfile, FacultyProfile

# Register your models here.


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'roll_no', 'course', 'branch')
    list_display_links = ('user', 'roll_no')
    list_filter = ('user', 'course', 'branch')
    search_fields = ('user', 'roll_no', 'course', 'branch')
    list_max_show_all = 100

    fieldsets = (
        (None, {'fields': ('user', 'roll_no', 'course', 'branch', 'icard', 'phoneno', 'pic')}),
    )


class FacultyProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'department', 'position',)
    list_display_links = ('user', 'department')
    list_filter = ('department', 'position')
    search_fields = ('user', 'department', 'position',)
    list_max_show_all = 100

    fieldsets = (
        (None, {'fields': ('user', 'department', 'position', 'pic')}),
    )


admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(FacultyProfile, FacultyProfileAdmin)
