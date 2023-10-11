from django.db import models
from django.urls import reverse


class ContactModel(models.Model):
    name = models.CharField(max_length=256)
    email = models.EmailField()
    message = models.TextField()
    date_created = models.DateTimeField(auto_now=True)
    is_read_by_admin = models.BooleanField(null=True, default=False)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('contact-page')
