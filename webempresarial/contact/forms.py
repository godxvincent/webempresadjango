from django import forms
# https://docs.djangoproject.com/en/2.0/topics/forms/
# https://docs.djangoproject.com/en/2.0/ref/forms/fields/#built-in-field-classes


class ContactForms(forms.Form):
    name = forms.CharField(label='Nombre', required=True)
    email = forms.EmailField(label='Email', required=True)
    content = forms.CharField(label='Contenido', required=True,
                              widget=forms.Textarea)
