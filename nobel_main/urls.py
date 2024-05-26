from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns

from .security import login_view, logout_view
from .yasg import urlpatterns as doc_urls

urlpatterns = [
    path('i18n/', include("django.conf.urls.i18n")),
    path('accounts/login/', login_view, name='login'),
    path('accounts/logout/', logout_view, name='logout'),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    # path('admin_tools_stats/', include('admin_tools_stats.urls')),
]

urlpatterns += i18n_patterns(
    path('admin/', admin.site.urls),
    path('products/', include('product.urls'), name='products'),
    path('vacancy/', include('vacancy.urls'), name='vacancy'),
    path('others/', include('other.urls'), name='other'),
)

if 'rosetta' in settings.INSTALLED_APPS:
    urlpatterns += [
        path('rosetta/', include('rosetta.urls'))
    ]

urlpatterns += doc_urls
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
