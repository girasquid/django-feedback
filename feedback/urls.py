from django.conf.urls.defaults import *

from views import leave_feedback

urlpatterns = patterns('',
    url(r'^$', views.leave_feedback, name='leave-feedback'),
)