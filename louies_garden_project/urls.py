from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('louies_garden_app/', include('louies_garden_app.urls')),
]
