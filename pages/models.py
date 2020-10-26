from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse
from django.utils.text import slugify
from django.contrib.auth.models import User, Group
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

class Contact(models.Model):
    name =      models.CharField(max_length=100)
    mail =      models.CharField(max_length=50)
    message =   models.CharField(max_length=500)
    date =      models.DateField(auto_now=True)

    def __str__(self):
        return self.name + ' | ' + self.date

class Alumni_Status(models.Model):
    tag = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.tag

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    picture = models.ImageField(blank=True)
    telephone = models.CharField(max_length=200, blank=True, null=True)
    alumni_status = models.OneToOneField(Alumni_Status, on_delete=models.CASCADE, default=None, blank=True, null=True)

    def __str__(self):
        return self.user.first_name + " " + self.user.last_name

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

class Payment(models.Model):
    user_payment = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True)
    reason = models.CharField(max_length=300)
