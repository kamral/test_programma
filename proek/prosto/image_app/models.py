from django.db import models

# Create your models here.
class Flowers(models.Model):
    title = models.CharField(max_length=128)
    photo = models.ImageField(upload_to='', blank=True)

    planting_depth = models.PositiveIntegerField(help_text='cm', default=0)

    flowers_color = models.CharField(max_length=128)
    mature_height = models.PositiveIntegerField(help_text='cm', default=0)
    bulb_size = models.PositiveIntegerField(help_text='cm', default=0)
    bulb_spacing = models.PositiveIntegerField(help_text='cm', default=0)

    description = models.TextField()

    poison_toxic_for_animals = models.BooleanField()
    slug = models.SlugField(unique=True)

    @property
    def photo_url(self):
        if self.photo and hasattr(self.photo, 'url'):
            return self.photo.url

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Flowers, self).save(*args, **kwargs)

    def __str__(self):
        information = "\nTitle: "+str(self.title)
        return information