from django.urls import path, include
from django.contrib import admin
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('oauth2/', include('janus.urls')),
    path('', views.home, name='home'),
]
