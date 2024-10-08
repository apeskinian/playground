from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, "Owned"), (1, "Wishlist"))

class Watch(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='watch_owner')
    make = models.CharField(max_length=100)
    collection = models.CharField(max_length=100, blank=True)
    model = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    status = models.IntegerField(choices=STATUS)
    purchased_on = models.DateField(null=True, blank=True)
    image = CloudinaryField('image', default='placeholder', asset_folder='/watches/')

    def __str__(self):
        return f"{self.make} {self.model}"