from django.conf.urls import url
from .views import ProfileView,  ProjectView
from rest_framework import routers


urlpatterns = [
    url(r'^profile', ProfileView, name='profileview'),
    url(r'^project', ProjectView, name='projectView'),

]
