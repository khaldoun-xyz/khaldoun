from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path

from khaldoun import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.index, name="index"),
    path("imprint/", views.imprint, name="imprint"),
]

urlpatterns += staticfiles_urlpatterns()
