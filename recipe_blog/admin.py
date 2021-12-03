from django.contrib import admin
from .models import Recipe, Ingredients
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Recipe)
class RecipeAdmin(SummernoteModelAdmin):
    summernote_fields = ('content', 'excerpt')


admin.site.register(Ingredients)