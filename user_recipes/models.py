from django.db import models


class UserCreation(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    content = models.TextField()
    ingredients_list = models.TextField(blank=True)
    PUBPRI = ((0, "Private"), (1, "Public"))
    public_private = models.IntegerField(choices=PUBPRI, default=0)

    def __str__(self):
        return self.title
