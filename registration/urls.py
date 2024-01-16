import os
from django.contrib import admin
from django.urls import path, include
from app1 import views
from django.conf.urls.static import static
from django.conf import settings




urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('' , include('app1.urls')),
    
    path('report/', include('reportapp.urls')),
      
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)