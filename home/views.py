from django.shortcuts import render


# Create your views here.


def home(request):

    print("[0 - REQUESTS]")

    context = {
        'text': 'Olá, está é a pagina home',
        'title': 'Home',
    }

    return render(
        request,
        "home/index.html",
        context,
    )
