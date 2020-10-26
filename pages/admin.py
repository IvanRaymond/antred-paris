from django.contrib import admin
from .models import Event, Profile, Alumni_Status, Payment

# Register your models here.
admin.site.register(Event)
admin.site.register(Alumni_Status)
admin.site.register(Profile)
admin.site.register(Payment)