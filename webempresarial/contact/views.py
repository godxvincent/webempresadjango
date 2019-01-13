from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import ContactForms

# Create your views here.


def contact(request):
    contactForm = ContactForms()
    if request.method == "POST":
        contactForm = ContactForms(data=request.POST)
        if contactForm.is_valid():
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            content = request.POST.get('content', '')
            return redirect(reverse('contact')+"?ok")

    return render(request, "contact/contact.html", {'contactForm': contactForm})
