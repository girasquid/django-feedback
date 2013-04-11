from django.conf import settings
from feedback.forms import AnonymousFeedbackForm, FeedbackForm


def feedback_form(request):
    feedback_form = None
    if request.user.is_authenticated():
        feedback_form = FeedbackForm()
    elif getattr(settings, 'ALLOW_ANONYMOUS_FEEDBACK', True):
        feedback_form = AnonymousFeedbackForm()
    return {'feedback_form': feedback_form}
