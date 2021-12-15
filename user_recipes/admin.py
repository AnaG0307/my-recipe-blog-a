from django.contrib import admin
from .models import UserCreation
from django_summernote.admin import SummernoteModelAdmin


@admin.register(UserCreation)
class UserCreationAdmin(SummernoteModelAdmin):

    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content', 'ingredients_list')
    search_fields = ['title', 'content']
    list_filter = ['title', 'content']
