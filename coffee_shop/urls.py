from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', include('products.urls')),
    path('admin/', admin.site.urls),
    path('usuarios/', include('users.urls')),
    path('ordenes/', include('orders.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
