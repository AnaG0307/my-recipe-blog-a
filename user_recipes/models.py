from django.db import models
from cloudinary.models import CloudinaryField


class UserCreation(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    image = CloudinaryField('image', default='placeholder')
    content = models.TextField()
    ingredients_list = models.TextField(blank=True)
    PUBPRI = ((0, "Private"), (1, "Public"))
    public_private = models.IntegerField(choices=PUBPRI, default=0)

    def __str__(self):
        return self.title
