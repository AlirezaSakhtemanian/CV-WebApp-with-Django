from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings


def send_mail_service(subject, context, to, template_name):
    try:
        message_html = render_to_string(template_name, context)
        plain_message = strip_tags(message_html)
        from_email = settings.EMAIL_HOST_USER
        send_mail(subject, plain_message, from_email, recipient_list=[to], html_message=message_html)
    except:
        pass
