
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('publications/', include('publications.urls')),
    path('admin/', admin.site.urls),
]
