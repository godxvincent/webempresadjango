from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.mail import EmailMessage
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
            email = EmailMessage(
                "La caffietiera: Nuevo mensaje de contacto",
                "De {} <{}>\n\n Escribió: \n\n{}".format(name, email, content),
                "no-contestar@inbox.mailtrap.io",
                ["godxvincent@gmail.com"],
                reply_to=[email]
            )
            try:
                email.send()
                return redirect(reverse('contact')+"?ok")
            except:
                # hubo un fallo
                return redirect(reverse('contact')+"?fail")

    return render(request, "contact/contact.html", {'contactForm': contactForm})
