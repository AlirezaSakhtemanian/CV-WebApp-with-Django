from django import forms
from .models import ContactModel
from django.utils.translation import gettext_lazy as _


class ContactModelForm(forms.ModelForm):
    class Meta:
        model = ContactModel
        fields = ('name', 'email', 'message')
        widgets = {
            'name': forms.TextInput(attrs={
                'class': "form-control",
            }),
            'email': forms.EmailInput(attrs={
                'class': "form-control",
            }),
            'message': forms.Textarea(attrs={
                'class': "form-control",
            }),
        }
        labels = {
            'name': _('name'),
            'email': _('email'),
            'message': _('message')
        }
