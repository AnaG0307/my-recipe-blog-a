from django.contrib import admin
from .models import Recipe, Ingredient
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Recipe, Ingredient)
class RecipeAdmin(SummernoteModelAdmin):
    summernote_fields = ('content', 'excerpt')


# admin.site.register(Ingredients)