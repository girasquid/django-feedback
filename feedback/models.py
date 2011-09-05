# vim: tabstop=4 expandtab autoindent shiftwidth=4 fileencoding=utf-8

from django.utils.translation import ugettext_lazy as _

from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.conf import settings

class BaseFeedback(models.Model):
    class Meta:
        abstract = True
        ordering = ['-time']

    type    = models.CharField(choices=settings.FEEDBACK_CHOICES, max_length=100, verbose_name=_('Type'))
    message = models.TextField(verbose_name=_('Message'))
    time    = models.DateTimeField(auto_now_add=True, verbose_name=_('Time'))
    
    def __unicode__(self):
        return self.message

    def get_absolute_url(self):
        return reverse('admin:view-feedback', args=[self.id])


class Feedback(BaseFeedback):
    user = models.ForeignKey(User, verbose_name=_('User'))


class AnonymousFeedback(BaseFeedback):
    user = models.ForeignKey(User, verbose_name=_('User'), null=True, blank=True, default=None)

# EOF

