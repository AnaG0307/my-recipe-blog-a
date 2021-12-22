from django.contrib import admin
from .models import UserRecipe


@admin.register(UserRecipe)
class UsersRecipes(admin.ModelAdmin):
    list_display = ('author_user', 'title', 'created_on', 'id')
    list_filter = ('name', 'created_on')
    search_fields = ('name', 'email')
