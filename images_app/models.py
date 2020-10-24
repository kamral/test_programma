from PIL import Image
from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from django.urls import reverse
# Create your models here.

class Post(models.Model):
    image=models.CharField(max_length=1024,blank=True)
    title=models.CharField(max_length=1024,)
    cover = models.ImageField(upload_to='images/',blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        super(Post, self).save(*args, **kwargs)
        # Выбор картинки
        img = Image.open(self.cover.path)
        # Условие
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.cover.path)




    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])
