from django.contrib import admin
from .models import Post, Comment
from import_export.admin import ImportExportModelAdmin, ImportExportActionModelAdmin

admin.site.site_header = 'Career And Counseling Cell'
# Register your models here.


class InlineComments(admin.TabularInline):
    model = Comment


class PostAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
    inlines = [InlineComments]
    list_display = ('title', 'description', 'date',)
    list_display_links = ('title', 'description')
    list_editable = ('date',)
    list_filter = ('date',)
    search_fields = ('title', 'description', 'content', 'date')
    list_max_show_all = 50


class CommentAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
    list_display = ('comment_user', 'article', 'comment_content', 'comment_date')
    list_display_links = ('comment_user', 'article')
    list_editable = ('comment_content',)
    list_filter = ('comment_date', 'article')
    search_fields = ('user', 'article', 'comment_content', 'comment_date')


admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)

