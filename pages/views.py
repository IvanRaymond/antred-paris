from django.shortcuts import render, get_object_or_404, redirect
from .form import ContactForm, MemberForm
from .models import Event
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


def event_detail_view(request, id):
    obj = get_object_or_404(Event, id=id)
    context = {
        "object": obj
    }
    return render(request, "event/event_detail.html", context)


def event_list_view(request):
    queryset = Event.objects.all()
    context = {
        'events': queryset
    }
    return render(request, "event/event.html", context)


def members_join_view(request):
    form = MemberForm(request.POST or None)
    if form.is_valid():
        # fetch first_year checkbox value
        # if ticked display additionnal message that payment is optional and do a form.save()
        # form.save()
        first_year = False
        if request.POST.get('div_id_first_year', True):
            first_year = 'on'
        status = request.POST['status']

        if first_year == 'on' and status == 'étudiant':

            # Uncomment on production
            # form.save()
            return render(request, "member/payment_member.html", {
                'first_year': True
            })
        else:

            return render(request, "member/payment_member.html", {
                'first_year': False
            })

    context = {
        'form': form,
        'button_label': "Confirmer"
    }

    return render(request, "member/add_member.html", context)

# How to get Paypal validation after payment
# Add to DB after paypal validation

def information_view(request):
    # pass the information from DB
    context = {

    }

    return render(request, "information/information.html", context)
