from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.conf import settings

class Feedback(models.Model):
    
    class Meta:
        
        ordering = ['-time']
    
    user    = models.ForeignKey(User)
    type    = models.CharField(choices=settings.FEEDBACK_CHOICES, max_length=100)
    message = models.TextField()
    time    = models.DateTimeField(auto_now_add=True)
    
    def __unicode__(self):
        return self.message

    def get_absolute_url(self):
        return reverse('admin:view-feedback', args=[self.id])