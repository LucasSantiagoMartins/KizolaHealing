from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include('user.urls')),
    path('patient/', include('patient.urls')),
    path('health/', include('health.urls')),
    path('management/', include('management.urls')),


]
