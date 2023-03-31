from django.shortcuts import render
from home.models import *
def home(request):
    about = About.objects.all().last()
    donation_title = Donation_Title.objects.all().last()
    helpers = Helpers.objects.all()
    
    return render(request, "home/index.html", 
                  context={'about': about, 'donation_title': donation_title,
                           'helpers': helpers})
