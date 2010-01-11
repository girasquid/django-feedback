from forms import FeedbackForm
from django.http import HttpResponseRedirect
from django.template import RequestContext

def leave_feedback(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            request.user.message_set.create(message="Your feedback has been saved successfully.")
            return HttpResponseRedirect(request.POST.get('next', request.META.get('HTTP_REFERER', '/')))
    else:
        form = FeedbackForm(request.GET)
    return render_to_response('feedback/feedback_form.html', {'form': form}, context_instance=RequestContext(request))