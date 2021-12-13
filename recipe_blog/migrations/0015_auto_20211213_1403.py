# Generated by Django 3.2.9 on 2021-12-13 14:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipe_blog', '0014_alter_recipe_list'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shopping_list',
            name='ingredient_added',
        ),
        migrations.RemoveField(
            model_name='shopping_list',
            name='user_list',
        ),
        migrations.RemoveField(
            model_name='recipe',
            name='ingredients',
        ),
        migrations.RemoveField(
            model_name='recipe',
            name='public_private',
        ),
        migrations.DeleteModel(
            name='Blog_user',
        ),
        migrations.DeleteModel(
            name='Ingredient',
        ),
        migrations.DeleteModel(
            name='Shopping_list',
        ),
    ]
