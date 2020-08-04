from django import forms
from django.core.validators import RegexValidator
from .models import Member

alpha = RegexValidator(r"^[a-zA-Z']*$", 'Les caractères numériques sont interdit.')
alphanumeric = RegexValidator(r"^['0-9a-zA-Z]*$", 'Caractères interdit.')
numeric = RegexValidator(r"^[0-9+-]*$", 'Les caractères alpha sont interdit.')

class MemberForm(forms.ModelForm):

    status=[
        ('','Choisissez un Statut'),
        ('étudiant','Étudiant'),
        ('salarié','Salarié'),
        ('entrepreneur','Entrepreneur'),
        ('autre','Autre'),
    ]

    name = forms.CharField(
        required=True,
        label='',
        validators=[alpha],
        widget=forms.TextInput(
            attrs={
                "placeholder":"Nom",
                "oninvalid": "this.setCustomValidity('Ce champ est obligatoire')",
                "oninput": "setCustomValidity('')",
                "class": "form-control border-0"
            }
        )
    )

    mail = forms.CharField(
        required=True,
        label='',
        widget=forms.TextInput(
            attrs={
                "placeholder": "Mail",
                "oninvalid": "this.setCustomValidity('Ce champ est obligatoire')",
                "oninput": "setCustomValidity('')",
                "class": "form-control border-0"
            })
    )

    phone_number    = forms.CharField(
        required=False,
        label='',
        validators=[numeric],
        widget=forms.TextInput(
            attrs={
                "placeholder": "Téléphone",
                "oninvalid": "this.setCustomValidity('Entré une information valide')",
                "oninput": "setCustomValidity('')",
                "class": "form-control border-0"
            })
    )

    status = forms.ChoiceField(
        error_messages={'required': 'Choisissez une option dans la liste'},
        required=True,
        label='',
        initial='none',
        choices=status,
        widget=forms.Select(
            attrs={
                "oninvalid": "this.setCustomValidity('Choisissez une option dans la liste')",
                "oninput": "setCustomValidity('')",
                "class": "form-control border-0"
            })
        )

    first_year = forms.CharField(
        label='Première Année ?',
        required=False,
        widget=forms.CheckboxInput(
            attrs={
                "class": "form-check-input"
            }
        )
    )

    class Meta:
        model = Member
        fields = [
            'name',
            'mail',
            'phone_number',
            'status',
            'first_year'
        ]