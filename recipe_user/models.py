# from django.db import models
# from django.contrib.auth.models import User
# from cloudinary.models import CloudinaryField


# class UserRecipe(models.Model):
#     name = models.CharField(max_length=50)
#     email = models.EmailField(max_length=100)
#     title = models.CharField(max_length=200, unique=True)
#     slug = models.SlugField(max_length=100, unique=True)
#     image = CloudinaryField('image', default='placeholder')
#     content = models.TextField()
#     ingredients_list = models.TextField(blank=True)
#     PUBPRI = ((0, "Private"), (1, "Public"))
#     public_private = models.IntegerField(choices=PUBPRI, default=0)
#     created_on = models.DateField(auto_now_add=True)
#     updated_on = models.DateField(auto_now=True)

#     def __str__(self):
#         return self.title
