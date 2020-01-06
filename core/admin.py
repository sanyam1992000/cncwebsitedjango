from django.contrib import admin
from .models import SlideShowPic, ContactUs, Member


class ContactUsAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phoneno', 'query')
    list_display_links = ('name', 'email', 'phoneno')
    list_filter = ('name', 'phoneno')
    search_fields = ('name', 'email', 'phoneno', 'query')
    list_max_show_all = 20

    fieldsets = (
        (None, {'fields': ('name', 'email', 'phoneno', 'query')}),
    )


admin.site.register(Member)
admin.site.register(SlideShowPic)
admin.site.register(ContactUs, ContactUsAdmin)
