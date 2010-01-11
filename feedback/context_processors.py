from feedback.forms import FeedbackForm

def feedback_form(request):
    feedback_form = None
    if request.user.is_authenticated():
        feedback_form = FeedbackForm(initial={'user':request.user})
    return {'feedback_form': feedback_form}