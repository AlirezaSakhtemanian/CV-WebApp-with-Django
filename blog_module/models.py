from django.db import models
from django.urls import reverse


class BlogModel(models.Model):
    title = models.CharField(max_length=256)
    date = models.DateTimeField(auto_now_add=True, editable=False)
    slug = models.SlugField(max_length=300, null=False, default='', db_index=True)
    short_description = models.TextField(max_length=2000)
    image_main = models.ImageField(upload_to='images/blog', null=True)
    is_deleted = models.BooleanField(default=False, db_index=True)
    code_language = models.CharField(max_length=20, null=True, blank=True)
    code = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog-content-page', args=[self.slug])


class BlogDescriptionAndImage(models.Model):
    blog = models.ForeignKey(BlogModel, on_delete=models.CASCADE, related_name='description_images')
    title_header = models.CharField(max_length=200, default='', null=True, blank=True)
    title_header_slug = models.SlugField(null=True, blank=True)
    description = models.TextField(null=True, blank=True, db_index=True)
    image = models.ImageField(upload_to='images/blog', null=True, blank=True)
    image_size = models.CharField(max_length=10, default="500x250")

    def __str__(self):
        return f'{self.blog.title}'


class BlogTitlesHeader(models.Model):
    blog = models.ForeignKey(BlogModel, on_delete=models.CASCADE, related_name='title_header')
    title = models.CharField(max_length=200, null=True, blank=True)
    slug = models.SlugField(null=True, blank=True)

    def __str__(self):
        return f'{self.blog.title} - {self.title}'


class BlogCommentModel(models.Model):
    blog = models.ForeignKey(BlogModel, on_delete=models.CASCADE)
    parent = models.ForeignKey('BlogCommentModel', null=True, blank=True, on_delete=models.CASCADE)
    create_date = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=20, db_index=True)
    email = models.EmailField(db_index=True)
    text = models.TextField(db_index=True)

    def __str__(self):
        return f'{self.name}--{self.parent_id}'
