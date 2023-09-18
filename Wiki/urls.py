from .views import home, second
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = ([
    path('', home, ),
    path('docs-page', second, ),

])

urlpatterns += \
    ([
    path("ckeditor5/", include('django_ckeditor_5.urls'), name="ck_editor_5_upload_file"),
]
+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT))