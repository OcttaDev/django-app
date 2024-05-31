from django.shortcuts import render


# Create your views here.


def home(request):

    print("[0 - REQUESTS]")
    return render(
        request,
        template_name="home/index.html"
    )
