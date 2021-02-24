from django.db import models

# Create your models here.
class ImageGallery(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='portfolio/images/')
    url = models.URLField(blank=True) # to make it optional

    def __str__(self):
        return self.title
    