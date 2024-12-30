from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path

from khaldoun import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.index, name="index"),
    path("growth", views.growth, name="growth"),
]

urlpatterns += staticfiles_urlpatterns()

