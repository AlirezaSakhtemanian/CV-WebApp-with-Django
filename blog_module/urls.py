from django.urls import path

from . import views

urlpatterns = [
    path('<slug:slug>', views.BlogDetailView.as_view(), name='blog-content-page'),
]
