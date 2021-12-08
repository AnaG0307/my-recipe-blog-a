from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from taggit.managers import TaggableManager


STATUS = ((0, "Draft"), (1, "Published"))
PUBPRI = ((0, "Private"), (1, "Public"))


class Ingredient(models.Model):
    ingr_name = models.CharField(max_length=200, unique=True)
    type = models.CharField(max_length=200)

    class Meta:
        ordering = ['ingr_name']

    def __string__(self):
        return self.ingr_name


class Recipe(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="recipe_post", default=0
        )
    main_image = CloudinaryField('image', default='placeholder')
    excerpt = models.CharField(max_length=250, blank=True)
    content = models.TextField()
    ingredients = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    tag = TaggableManager()
    likes = models.ManyToManyField(User, related_name='blog_likes', blank=True)
    created_on = models.DateField(auto_now_add=True)
    updated_on = models.DateField(auto_now=True)
    approved = models.IntegerField(choices=STATUS, default=0)
    public_private = models.IntegerField(choices=PUBPRI, default=0)
    featured = models.BooleanField(default=False)

    class Meta:
        ordering = ['featured', '-created_on']

    def __str__(self):
        return self.title

    def number_of_likes(self):
        return self.likes.count()


class Blog_user(models.Model):
    username = models.CharField(max_length=200, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    created_recipes = models.ForeignKey(Recipe, on_delete=models.CASCADE)

    def __str__(self):
        return self.username


class Comment(models.Model):
    name = models.CharField(max_length=50)
    content = models.TextField()
    created_on = models.DateField(auto_now_add=True)
    recipe_title = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    approved = models.BooleanField(default=False)
    email = models.EmailField(max_length=100)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return self.name


class Tag(models.Model):
    Tag_name = models.CharField(max_length=100)


class Shopping_list(models.Model):
    user_list = models.ForeignKey(Blog_user, on_delete=models.CASCADE)
    ingredient_added = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.DecimalField(max_digits=6, decimal_places=2)
    to_buy = models.BooleanField(default=False)
