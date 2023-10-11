from modeltranslation.translator import TranslationOptions, register

from .models import SiteSetting, Projects, Degrees


@register(SiteSetting)
class BlogTranslation(TranslationOptions):
    fields = ['name', 'address', 'about_me_short_des', 'about_me_long_des']


@register(Projects)
class BlogTranslation(TranslationOptions):
    fields = ['title', 'short_description']


@register(Degrees)
class BlogTranslation(TranslationOptions):
    fields = ['title']
