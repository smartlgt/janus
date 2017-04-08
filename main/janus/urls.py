"""janus URL Configuration
"""
from django.conf.urls import url, include

from janus import views

urlpatterns = [
    url(r'^o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    url(r'^o/profile/$', views.ProfileView.as_view(), name="profile"),

    url('^accounts/', include('django.contrib.auth.urls')),
    url(r'^', views.index, name='index'),
]
