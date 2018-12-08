from django.conf.urls import url
from fbapi import views
from django.urls import path
from .views import ListSongsView

urlpatterns = [
    url(r'^hi/$', views.hi, name='hi'),
    path('songs/', ListSongsView.as_view(), name="songs-all")
]
