# Generated by Django 3.2.9 on 2021-12-09 20:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recipe_blog', '0008_auto_20211209_1433'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='recipe_title',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='recipe_blog.recipe'),
        ),
    ]
