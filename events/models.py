from django.db import models
from django.urls import reverse

# Create your models here.


class Event(models.Model):
    title = models.CharField(blank=False, max_length=120) # max_length is required
    images = models.ImageField(upload_to='events', blank=True)
    description = models.TextField(blank=False)
    date = models.DateTimeField(blank=False)

    def __str__(self):
        return '%s | %s' % (self.title, str(self.date))

    def get_absolute_url(self):
        return reverse("events:event-detail", kwargs={"id": self.id})