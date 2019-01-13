from django import forms
# https://docs.djangoproject.com/en/2.0/topics/forms/
# https://docs.djangoproject.com/en/2.0/ref/forms/fields/#built-in-field-classes


class ContactForms(forms.Form):
    name = forms.CharField(label='Nombre', required=True,
                           widget=forms.TextInput(
                               attrs={'class': 'form-control',
                                      'placeholder': 'Escribe tu nombre'}
                           ), min_length=3, max_length=100)
    email = forms.EmailField(label='Email', required=True,
                             widget=forms.EmailInput(
                                 attrs={'class': 'form-control',
                                        'placeholder': 'Escribe tu email'}
                             ), min_length=3, max_length=100)
    content = forms.CharField(label='Contenido', required=True,
                              widget=forms.Textarea(
                                  attrs={'class': 'form-control', 'rows': 3,
                                         'placeholder': 'Escribe tu mensaje'}
                              ), min_length=10, max_length=300)
