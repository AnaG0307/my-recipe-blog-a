from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from taggit.managers import TaggableManager


STATUS = ((0, "Draft"), (1, "Published"))


class Recipe(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="recipe_post", default=0
        )
    main_image = CloudinaryField('image', default='placeholder')
    excerpt = models.CharField(max_length=250, blank=True)
    content = models.TextField()
    list = models.TextField(blank=True)
    tag = TaggableManager()
    likes = models.ManyToManyField(User, related_name='blog_likes', blank=True)
    favourite = models.ManyToManyField(
        User,
        related_name='favourites',
        default=None,
        blank=True
        )
    BEGINNER = 'B'
    INTERMEDIATE = 'I'
    ADVANCED = 'A'
    LEVEL = [
        ("BEGINNER", "Beginner"),
        ("INTERMEDIATE", "Intermediate"),
        ("ADVANCED", "Advanced"),
        ]
    difficulty = models.CharField(
        max_length=20,
        choices=LEVEL,
        default=BEGINNER,
        null=True
        )
    time = models.CharField(max_length=50, blank=True)
    created_on = models.DateField(auto_now_add=True)
    updated_on = models.DateField(auto_now=True)
    approved = models.IntegerField(choices=STATUS, default=0)
    featured = models.BooleanField(default=False)

    class Meta:
        ordering = ['featured', '-created_on']

    def __str__(self):
        return self.title

    def number_of_likes(self):
        return self.likes.count()


class Comment(models.Model):
    name = models.CharField(max_length=50)
    content = models.TextField()
    created_on = models.DateField(auto_now_add=True)
    recipe_title = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name="comments"
        )
    approved = models.BooleanField(default=False)
    email = models.EmailField(max_length=100)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f'Comment {self.content} by {self.name}'

    def number_of_comments(self):
        return self.approved.count()


class Tag(models.Model):
    Tag_name = models.CharField(max_length=100)
