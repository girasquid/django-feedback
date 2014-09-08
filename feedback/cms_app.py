#coding; utf8
from django.utils.translation import ugettext_lazy as _
from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool


class FeedbackApp(CMSApp):
    name = _('feedback')
    urls = ['feedback.urls']
    app_name = 'feedback'


apphook_pool.register(FeedbackApp)
