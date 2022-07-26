from django.shortcuts import render

# Create your views here.


def beforeyougo(request):
    """ A view to return the index page """

    return render(request, 'beforeyougo/beforeyougo.html')