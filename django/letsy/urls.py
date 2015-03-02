import letsy.views
import django_nopassword.urls
from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', letsy.views.home, name='home'),
    url(r'^accounts/', include(django_nopassword.urls)),
    url(r'^admin/', include(admin.site.urls)),
)
