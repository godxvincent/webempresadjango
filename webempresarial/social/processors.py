from .models import Link

# Documentación sobre procesadores de contexto.
# https://docs.djangoproject.com/en/2.0/ref/templates/api/#writing-your-own-context-processors


def context_procesor(request):
    social_context = {}
    for enlace in Link.objects.all():
        social_context[enlace.key] = enlace.urlRedSocial
    return social_context
