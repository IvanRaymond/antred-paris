from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .form import MemberForm
from .models import Member

# Create your views here.
def members_join_view(request):

    form = MemberForm(request.POST or None)
    if form.is_valid():
            # fetch first_year checkbox value
            # if ticked display additionnal message that payment is optional and do a form.save()
            #form.save()

        first_year = request.POST['first_year']
        status = request.POST['status']

        print(first_year)

        if first_year == 'on' and status == 'étudiant':

            #form.save()
            return render(request,"payment_member.html",{
                'first_year': True
            })
        else:
 

            return render(request,"payment_member.html",{
                'first_year': False
            })

    context = {
        'form': form,
        'button_label': "Confirmer"
    }

    return render(request,"add_member.html",context)


# How to get Paypal validation after payment
# Add to DB after paypal validation