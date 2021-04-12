from django.contrib import admin
from django.urls import path
from .views import index
from .views import resume


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('resume/', resume)
]
