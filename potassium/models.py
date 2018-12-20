from django.db import models


class GalleryImage(models.Model):
    title = models.CharField(max_length=128, unique=True)
    image = models.ImageField(upload_to="gallery")
    description = models.CharField(max_length=256, blank=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
