from django.contrib import admin
from .models import UserRecipe
from django_summernote.admin import SummernoteModelAdmin


@admin.register(UserRecipe)
class UsersRecipes(admin.ModelAdmin):
    list_display = ('title', 'created_on')
    list_filter = ('name', 'created_on')
    search_fields = ('name', 'email')
