from feedback.forms import FeedbackForm, AnonymousFeedbackForm

def feedback_form(request):
    feedback_form = None
    if request.user.is_authenticated():
        feedback_form = FeedbackForm()
    else:
        feedback_form = AnonymousFeedbackForm()

    return {'feedback_form': feedback_form}

