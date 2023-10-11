from django.contrib import admin

from .models import BlogModel, BlogCommentModel, BlogDescriptionAndImage, BlogTitlesHeader


class BlogDescriptionAndImageInline(admin.TabularInline):
    model = BlogDescriptionAndImage
    extra = 1
    prepopulated_fields = {
        'title_header_slug' : ('title_header', ),
    }


class BlogTitlesHeaderInline(admin.TabularInline):
    model = BlogTitlesHeader
    extra = 1
    prepopulated_fields = {
        'slug': ('title',),
    }


@admin.register(BlogModel)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'is_deleted',)
    list_filter = ('date', 'is_deleted')
    list_editable = ('is_deleted',)
    ordering = ('date',)
    prepopulated_fields = {
        'slug': ('title',),
    }
    inlines = [BlogDescriptionAndImageInline, BlogTitlesHeaderInline]


@admin.register(BlogCommentModel)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('blog', 'create_date', 'parent',)
    list_filter = ('blog', 'create_date')
    ordering = ('blog_id',)
