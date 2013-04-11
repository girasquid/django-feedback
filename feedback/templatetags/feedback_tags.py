from django.conf import settings
from django.template import Library, Node
from feedback.models import AnonymousFeedback, Feedback
from itertools import chain


register = Library()


@register.tag
def get_feedback(parser, token):
    '''
    {% get_feedback %}
    '''
    return FeedbackNode()


class FeedbackNode(Node):
    def render(self, context):
        feedback = [Feedback.objects.all()]
        if getattr(settings, 'ALLOW_ANONYMOUS_FEEDBACK', False):
            feedback.append(AnonymousFeedback.objects.all())
        # Flatten list of querysets and sort feedback by date.
        feedback = sorted(list(chain.from_iterable(feedback)),
                          key=lambda instance: instance.time, reverse=True)
        context['feedback'] = feedback
        return ''
