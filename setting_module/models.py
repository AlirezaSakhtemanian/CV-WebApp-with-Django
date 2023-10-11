from django.db import models


class SiteSetting(models.Model):
    is_main_setting = models.BooleanField(default=False, db_index=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    age = models.SmallIntegerField()
    address = models.CharField(max_length=300)
    about_me_short_des = models.TextField()
    about_me_long_des = models.TextField()
    picture = models.ImageField(upload_to='images/profile', null=True, blank=True)
    logo = models.ImageField(upload_to='images/logos', null=True, blank=True)
    telegram = models.CharField(max_length=200, null=True, blank=True)
    linkedin = models.CharField(max_length=200, null=True, blank=True)
    instagram = models.CharField(max_length=200, null=True, blank=True)
    github = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name


class Skills(models.Model):
    title = models.CharField(max_length=100)
    skill_percent = models.CharField(max_length=10)

    def __str__(self):
        return self.title


class Projects(models.Model):
    title = models.CharField(max_length=200)
    url = models.CharField(max_length=300, null=True, blank=True)
    image = models.ImageField(upload_to='images/projects', null=True, blank=True)
    short_description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title


class Degrees(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/degrees', null=True, blank=True)

    def __str__(self):
        return self.title
