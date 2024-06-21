
from django.contrib import admin
from django.urls import path

from webapp.views import index, about

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", index),
    path("about/", about)
]
