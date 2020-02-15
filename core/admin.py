from django.contrib import admin
from .models import SlideShowPic, ContactUs, Member
admin.site.site_header = 'Career And Counseling Cell'


class ContactUsAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phoneno', 'query')
    list_display_links = ('name', 'email', 'phoneno')
    list_filter = ('name', 'phoneno')
    search_fields = ('name', 'email', 'phoneno', 'query')
    list_max_show_all = 50

    fieldsets = (
        (None, {'fields': ('name', 'email', 'phoneno', 'query')}),
    )


class MembersAdmin(admin.ModelAdmin):
    list_display = ('user', 'userprofile', 'description', 'status')
    list_display_links = ('user', 'userprofile')
    list_filter = ('description', 'status')
    list_editable = ('description', 'status')
    search_fields = ('user', 'userprofile', 'description', 'status')
    list_max_show_all = 100

    fieldsets = (
        (None, {'fields': ('user', 'userprofile', 'description', 'status')}),
    )


class SlideShowPicAdmin(admin.ModelAdmin):
    list_display = ('title', 'image', 'description', 'url', 'number')
    list_display_links = ('title', 'description')
    list_filter = ('number',)
    list_editable = ('url', 'number')
    search_fields = ('title', 'image', 'description', 'url', 'number')
    list_max_show_all = 100

    fieldsets = (
        (None, {'fields': ('title', 'image', 'description', 'url', 'number')}),
    )


admin.site.register(Member, MembersAdmin)
admin.site.register(SlideShowPic, SlideShowPicAdmin)
admin.site.register(ContactUs, ContactUsAdmin)
