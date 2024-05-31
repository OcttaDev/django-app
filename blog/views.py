from django.shortcuts import render


# Create your views here.


def blog(request):
    print("[0 - REQUESTS]")
    return render(
        request,
        template_name='blog/index.html'
    )
