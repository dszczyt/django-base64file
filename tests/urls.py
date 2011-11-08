# -*- coding: utf-8 -*-
from django.conf.urls.defaults import patterns, url
from .views import AvatarCreateView

urlpatterns = patterns('tests.views',
                       url(r'^upload/$', AvatarCreateView.as_view(), name="upload"),
                      )
