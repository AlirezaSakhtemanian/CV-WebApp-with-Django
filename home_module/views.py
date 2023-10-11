from django.conf import settings
from django.http import HttpRequest, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView, View

from blog_module.models import BlogModel
from contact_module.forms import ContactModelForm
from setting_module.models import SiteSetting, Skills, Projects, Degrees
from utils.email_services import send_mail_service


class IndexView(View):
    def get(self, request: HttpRequest):
        contact_form = ContactModelForm()
        context = {
            'projects': Projects.objects.all(),
            'setting': SiteSetting.objects.filter(is_main_setting=True).first(),
            'degrees': Degrees.objects.all(),
            'skills': Skills.objects.all().order_by('-skill_percent'),
            'blogs': BlogModel.objects.filter(is_deleted=False).prefetch_related('description_images').all(),
            'form': contact_form
        }
        return render(request, 'home_module/home.html', context)

    def post(self, request: HttpRequest):
        contact_form = ContactModelForm(request.POST)
        if contact_form.is_valid():
            contact_form.save()
            name = contact_form.cleaned_data['name']
            email = contact_form.cleaned_data['email']
            message = contact_form.cleaned_data['message']
            context_email = {
                'email': email,
                'name': name,
                'message': message
            }
            send_mail_service("New Message From CONTACT-PAGE", context_email, settings.RECIPIENT_ADDRESS, 'email/contact_message_email.html')
            return HttpResponseRedirect(reverse_lazy('index-page'))

        context = {
            'projects': Projects.objects.all(),
            'setting': SiteSetting.objects.filter(is_main_setting=True).first(),
            'degrees': Degrees.objects.all(),
            'skills': Skills.objects.all().order_by('-skill_percent'),
            'blogs': BlogModel.objects.filter(is_deleted=False).prefetch_related('description_images').all(),
            'form': contact_form
        }
        return render(request, 'home_module/home.html', context)
