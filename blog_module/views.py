from django.http import HttpRequest
from django.shortcuts import render
from django.views import View

from .forms import BlogCommentForm
from .models import BlogModel, BlogCommentModel, BlogTitlesHeader


class BlogDetailView(View):
    def get(self, request: HttpRequest, slug):
        form = BlogCommentForm()
        blog = BlogModel.objects.filter(is_deleted=False, slug__iexact=slug).prefetch_related('description_images').first()
        context = {
            'form': form,
            'blog': blog,
            'comments': BlogCommentModel.objects.filter(blog_id=blog.id, parent=None).order_by('-create_date').prefetch_related(
                'blogcommentmodel_set'),
            'comments_count': BlogCommentModel.objects.filter(blog_id=blog.id).count(),
            'title_headers': BlogTitlesHeader.objects.filter(blog_id__exact=blog.id).all(),
        }
        return render(request, 'blog_module/blog_content.html', context)

    def post(self, request: HttpRequest, slug):
        form = BlogCommentForm(request.POST)
        blog = BlogModel.objects.filter(is_deleted=False, slug__iexact=slug).prefetch_related('description_images').first()
        if form.is_valid():
            name = form.cleaned_data.get('name')
            email = form.cleaned_data.get('email')
            message = form.cleaned_data.get('text')
            parent = form.cleaned_data.get('parent')
            if parent:
                new_comment = BlogCommentModel(blog_id=blog.id, parent_id=parent.id, name=name, email=email, text=message)
            else:
                new_comment = BlogCommentModel(blog_id=blog.id, name=name, email=email, text=message)
            new_comment.save()

        context = {
            'form': form,
            'blog': blog,
            'comments': BlogCommentModel.objects.filter(blog_id=blog.id, parent=None).order_by('-create_date').prefetch_related(
                'blogcommentmodel_set'),
            'comments_count': BlogCommentModel.objects.filter(blog_id=blog.id).count(),
            'title_headers': BlogTitlesHeader.objects.filter(blog_id__exact=blog.id).all(),
        }
        return render(request, 'blog_module/blog_content.html', context)
