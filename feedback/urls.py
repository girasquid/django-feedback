from django.conf.urls import url
from feedback.views import leave_feedback


urlpatterns = [
    url(r'^$', leave_feedback, name='feedback'),
]
