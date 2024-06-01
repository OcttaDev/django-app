from django.shortcuts import render


# Create your views here.


def blog(request):

    context = {
        'text': 'Olá, está é a pagina home',
        'title': 'Blog',
    }

    print("[0 - REQUESTS]")
    return render(
        request,
        'blog/index.html',
        context
    )
