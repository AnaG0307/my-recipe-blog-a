from django.contrib import admin
from .models import Recipe, Ingredient, Comment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Recipe)
class RecipeAdmin(SummernoteModelAdmin):
    search_fields = [
        'author',
        'title',
        'content',
        'created_on',
        'approved',
        'featured'
        ]
    list_display = ('author', 'title', 'created_on', 'approved', 'featured')
    date_hierarchy = 'created_on'
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('approved', 'created_on', 'featured')
    summernote_fields = ('content', 'excerpt', 'list',)
    actions = ['user_recipe_public', 'feature_recipe', 'approved']

    def user_recipe_public(self, request, queryset):
        queryset.update(approved=True)

    def feature_recipe(self, request, queryset):
        queryset.update(approved=True)


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    search_fields = ['ingr_name', 'type']
    list_display = ('ingr_name', 'type', 'id')
    list_filter = ('ingr_name', 'type')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    search_fields = ['name', 'email', 'recipe_title', 'created_on']
    list_display = ('name', 'email', 'recipe_title', 'created_on', 'approved')
    list_filter = ('name', 'email', 'recipe_title', 'created_on', 'approved')
    actions = ['comment_approved']

    def comment_approved(self, request, queryset):
        queryset.update(approved=True)
