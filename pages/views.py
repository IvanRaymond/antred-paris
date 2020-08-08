from django.shortcuts import render
from .form import ContactForm
from events.models import Event
import datetime
from django.utils import timezone
# Create your views here.


def home_view(request):
    queryset = Event.objects.all()
    now = timezone.now()
    next_event = None
    last_event = None

    for event in reversed(queryset):
        if event.date >= now:
            if next_event == None:
                next_event = event
            elif event.date <= next_event.date:
                next_event = event
        elif event.date < now:
            if last_event == None:
                last_event = event
            elif event.date > last_event.date:
                last_event = event


    context = {
        "next_event": next_event,
        "last_event": last_event
    }
    return render(request, "home.html", context)


def contact_view(request):
    form = ContactForm(request.POST or None)

    message_sent = False

    if form.is_valid():
        message_name = form['name']
        message_mail = form['mail']
        message = form['message']

        # send an email
        #        send_mail(
        #            'Message from ' + message_name, # subject
        #            message, # message
        #            message_mail, # from email
        #            ['nestaray@hotmail.com'], # to email
        #        )
        message_sent = True

        form = ContactForm()  # re rendering form after saving

    context = {
        'form': form,
        'button_label': "Envoyer",
        'message_sent': message_sent
    }
    return render(request, "contact_form.html", context)


def us_view(request):
    context = {

    }
    return render(request, "us.html", context)
