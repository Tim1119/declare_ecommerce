from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("admin/", admin.site.urls),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = 'Declare Ecommerce'
admin.site.site_title = 'Declare Ecommerce Portal'
admin.site.index_title = 'Welcome to Declare Ecommerce Portal'
