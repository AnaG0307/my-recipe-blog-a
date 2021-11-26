from django.db import models
from cloudinary.models import CloudinaryField
from taggit.managers import TaggableManager


STATUS_APPROVED = ((0, "Draft"), (1, "Published"))
STATUS_PUBPRI = ((0, "Private"), (1, "Public"))


class Recipe(models.Model):
    title = models.CharField(max_length=200, unique=True)
    content = models.TextField()
    ingredients = models.TextField()
    excerpt = models.CharField(max_length=250)
    main_image = CloudinaryField('image', default='placeholder')
    tag = TaggableManager()
    slug = models.SlugField(max_length=50, unique=True)
    # author = models.
    # likes = models.ManyToManyField(User, related_name='blogpost_like')
    created_on = models.DateField(auto_now_add=True)
    updated_on = models.DateField(auto_now=True)
    approved = models.IntegerField(choices=STATUS_APPROVED, default=0)
    public_private = models.IntegerField(choices=STATUS_PUBPRI, default=0)
    featured = models.BooleanField(default=False)