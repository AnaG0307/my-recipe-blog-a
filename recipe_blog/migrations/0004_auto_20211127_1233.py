# Generated by Django 3.2.9 on 2021-11-27 12:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recipe_blog', '0003_auto_20211127_1025'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog_user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=200, unique=True)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Ingredients',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ingr_name', models.CharField(max_length=200, unique=True)),
                ('type', models.CharField(max_length=200)),
            ],
            options={
                'ordering': ['ingr_name'],
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Tag_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterModelOptions(
            name='recipe',
            options={'ordering': ['featured', '-created_on']},
        ),
        migrations.CreateModel(
            name='Shopping_list',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.DecimalField(decimal_places=2, max_digits=6)),
                ('to_buy', models.BooleanField(default=False)),
                ('ingredient_added', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipe_blog.ingredients')),
                ('user_list', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipe_blog.blog_user')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('content', models.TextField()),
                ('created_on', models.DateField(auto_now_add=True)),
                ('approved', models.BooleanField(default=False)),
                ('email', models.EmailField(max_length=100)),
                ('recipe_title', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipe_blog.recipe')),
            ],
            options={
                'ordering': ['created_on'],
            },
        ),
        migrations.AddField(
            model_name='blog_user',
            name='created_recipes',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipe_blog.recipe'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='ingredients',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipe_blog.ingredients'),
        ),
    ]
