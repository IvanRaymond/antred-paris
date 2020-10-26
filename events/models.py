from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.


class Event(models.Model):
    title = models.CharField(blank=False, max_length=120) # max_length is required
    images = models.ImageField(upload_to='events', blank=True)
    description = models.TextField(blank=False)
    date = models.DateTimeField(blank=False)
    slug = models.SlugField(null=True, blank=True)

    def __str__(self):
        return '%s | %s' % (self.title, str(self.date))

    def save(self, *args, **kwargs):
        slug = slugify(self.title)

        has_slug = Event.objects.filter(slug=slug).exists()
        count = 1
        while has_slug:
            count += 1
            slug = slugify(self.title) + '-' + str(count)
            has_slug = Event.objects.fitler(slug=slug).exists()

        self.slug = slug

        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("events:event-detail", kwargs={"id": self.id})