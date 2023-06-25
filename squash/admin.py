from django.contrib import admin
from .models import Comment, Club
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Comment)
class CommentAdmin(SummernoteModelAdmin):

    list_filter = ('created_on', 'user')
    summernote_fields = ('content')


@admin.register(Club)
class ClubAdmin(admin.ModelAdmin):

    list_display = ('club_name', 'created_on')




