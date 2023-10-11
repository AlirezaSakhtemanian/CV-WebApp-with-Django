from modeltranslation.translator import TranslationOptions, register

from .models import BlogModel, BlogDescriptionAndImage


@register(BlogModel)
class BlogTranslation(TranslationOptions):
    fields = ['title', 'short_description']


@register(BlogDescriptionAndImage)
class BlogTranslation(TranslationOptions):
    fields = ['description']
