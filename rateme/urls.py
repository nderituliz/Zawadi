from django.conf.urls import url
from .views import home, submission, profile, add_profile, search, view_project
from .views import SignUpView

urlpatterns = [
    url('signup/', SignUpView.as_view(), name='signup'),
    url(r'^$', home, name='home'),
    url(r'^sub', submission, name='submission'),
    url(r'^profile', profile, name='profile'),
    url(r'^add_profile', add_profile, name='add_profile'),
    url(r'^search', search, name='search'),
    url(r'^project/(?P<project_id>[0-9]+)', view_project, name='view_project')
]