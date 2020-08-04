from django.shortcuts import render

# Create your views here.


def information_view(request):
    # pass the information from DB
    context = {

    }

    return render(request, "information.html", context)
