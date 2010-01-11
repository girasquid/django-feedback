from django.conf.urls.defaults import *

from feedback.views import leave_feedback

urlpatterns = patterns('',
    url(r'^$', leave_feedback, name='leave-feedback'),
)