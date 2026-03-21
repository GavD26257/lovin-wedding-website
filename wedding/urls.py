from django.urls import re_path
from django.views.generic.base import RedirectView

from . import views

urlpatterns = [
    re_path(r'^$', RedirectView.as_view(url='reception/', permanent=True)),
    re_path(r'^reception/$', views.reception, name='reception'),
    re_path(r'^ceremony/$', views.ceremony, name='ceremony'),
]
