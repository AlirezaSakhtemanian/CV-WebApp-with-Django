from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [

]

urlpatterns += i18n_patterns(
    path('', include('home_module.urls')),
    path('blog/', include('blog_module.urls')),
    path('admin/', admin.site.urls),
    path('rosetta/', include('rosetta.urls')),
)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
