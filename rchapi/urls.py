from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    # API endpoints
    path('auth/', include("account.urls")),
    path('rchdata/', include("rchdata.urls")),
    path('newses/', include("rchnews.urls")),
    path('packages/', include("rchpackage.urls")),
    path('populations/', include("rchpopulation.urls")),
    path('articles/', include("rcharticle.urls")),
    path('promotions/', include("rchpromotion.urls")),
    path('events/', include("rcheven.urls")),
]

# Serve media only when DEBUG = True
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
