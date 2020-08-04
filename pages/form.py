from django import forms
from django.core.validators import RegexValidator
from .models import Contact

alpha = RegexValidator(r"^[a-zA-Z']*$", 'Les charactères numériques sont interdit.')
alphanumeric = RegexValidator(r"^['0-9a-zA-Z]*$", 'Charactères interdit')


class ContactForm(forms.ModelForm):

    name = forms.CharField(
        label= '',
        validators=[alpha],
        error_messages={'required': 'Ce champ est obligatoire.'},
        widget=forms.TextInput(
            attrs={
                "placeholder":"Nom",
                "oninvalid": "this.setCustomValidity('Ce champ est obligatoire')",
                "oninput": "setCustomValidity('')",
                "class": "form-control border-0"
            }
        )
    )

    mail = forms.EmailField(
        label='',
        error_messages={'required': 'Ce champ est obligatoire.'},
        widget=forms.TextInput(
            attrs={
                "type": "email",
                "placeholder": "Mail",
                "oninvalid": "this.setCustomValidity('Entrer une adresse email')",
                "oninput": "setCustomValidity('')",
                "class": "form-control border-0"
            }
        )
    )
    
    message = forms.CharField(
        label='',
        error_messages={'required': 'Ce champ est obligatoire.'},
        widget=forms.Textarea(
            attrs={
                "placeholder": "Message",
                "oninvalid": "this.setCustomValidity('Ce champ est obligatoire')",
                "oninput": "setCustomValidity('')",
                "class": "form-control border-0",
                "rows": "5"
            }
        )
    )

    class Meta:
        model = Contact
        fields = [
            'name',
            'mail',
            'message'
        ]