from django.db import models

# Create your models here.


class Contact(models.Model):
    name =      models.CharField(max_length=100)
    mail =      models.CharField(max_length=50)
    message =   models.CharField(max_length=500)
    date =      models.DateField(auto_now=True)

    def __str__(self):
        return self.name + ' | ' + self.date