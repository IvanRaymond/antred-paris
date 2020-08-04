from django.db import models

# Create your models here.
class Member(models.Model):
    name            = models.CharField(max_length=100)
    mail            = models.EmailField(max_length=254)
    phone_number    = models.CharField(blank=True,max_length=15)
    date_paid       = models.DateField(auto_now=True)
    status        = models.CharField(max_length=100)

    def __str__(self):
        return self.name