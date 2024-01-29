from django.urls import path
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView
from .views import index

urlpatterns = [
    path("favicon.ico", RedirectView.as_view(url=staticfiles_storage.url("images/favicon.ico"))),
    path('', index, name="home"),
]