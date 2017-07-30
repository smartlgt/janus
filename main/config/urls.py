from django.conf.urls import url, include
from django.contrib import admin

from janus import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^', include('janus.urls'))
]
