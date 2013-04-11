from django.conf.urls import patterns, url
from feedback.views import leave_feedback


urlpatterns = patterns('',
    url(r'^$', leave_feedback, name='feedback'),
)
