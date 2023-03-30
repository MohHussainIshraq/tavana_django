from django.shortcuts import render
from home.models import About
def home(request):
    about = About.objects.all().last()

    return render(request, "home/index.html", context={'about': about})
