from django import forms
from .models import BlogCommentModel
from django.utils.translation import gettext_lazy as _


class BlogCommentForm(forms.ModelForm):
    class Meta:
        model = BlogCommentModel
        fields = ('parent', 'name', 'email', 'text')
        widgets = {
            'parent': forms.TextInput(attrs={
                'type': "hidden",
            }),
            'name': forms.TextInput(attrs={
                'class': "form-control",
            }),
            'email': forms.EmailInput(attrs={
                'class': "form-control",
            }),
            'text': forms.Textarea(attrs={
                'class': "form-control",
            }),
        }
        labels = {
            'name': _('name'),
            'email': _('email'),
            'text': _('text')
        }
