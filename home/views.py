from django.shortcuts import render
from home.models import *
def home(request):
    about = About.objects.all().last()
    donation_title = Donation_Title.objects.all().last()
    helpers = Helpers.objects.all()
    details_donation = Details_Donations.objects.all().last()
    pictures = Pictures.objects.all()
    title_expenses = Title_Expenses.objects.all().last()
    expenses = Expenses.objects.all()
    contact = Contact.objects.all().last()
    footer = Footer.objects.all().last()

    return render(request, "home/index.html", 
                  context={'about': about, 'donation_title': donation_title,
                           'helpers': helpers, 'details_donations': details_donation,
                           'pictures': pictures, 'title_expenses': title_expenses,
                           'expenses': expenses, 'contact': contact,
                           'footer': footer})
