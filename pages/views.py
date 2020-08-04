from django.shortcuts import render
from .form import ContactForm
# Create your views here.


def home_view(request):
    context = {

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
