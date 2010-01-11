from django.template import Library, Node

from feedback.models import Feedback

register = Library()

@register.tag
def get_feedback(parser, token):
    """
    {% get_feedback %}
    """
    return FeedbackNode()
    
class FeedbackNode(Node):
    def render(self, context):
        context['feedback'] = Feedback.objects.all()
        return ''