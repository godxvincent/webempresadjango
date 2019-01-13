from django.shortcuts import render
from .forms import ContactForms

# Create your views here.


def contact(request):
    contactForm = ContactForms()
    return render(request, "contact/contact.html", {'contactForm': contactForm})
