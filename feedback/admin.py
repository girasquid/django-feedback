from django.conf import settings
from django.conf.urls import patterns, url
from django.contrib import admin
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext

from .models import AnonymousFeedback, Feedback


class FeedbackAdmin(admin.ModelAdmin):
    list_display = ['user', 'message', 'time', 'type', 'view']
    search_fields = ['user', 'message']
    list_filter = ['type', 'time']

    def view(self, obj):
        return "<a href='%s'>View</a>" % obj.get_absolute_url()

    view.allow_tags = True

    def get_urls(self):
        urls = super(FeedbackAdmin, self).get_urls()
        my_urls = patterns('',
            url(r'^view/(?P<feedback_id>\d+)/$',
                self.admin_site.admin_view(self.view_feedback),
                name='view-feedback'),
        )
        return my_urls + urls

    def view_feedback(self, request, feedback_id):
        feedback = get_object_or_404(Feedback, id=feedback_id)
        context = {'feedback': feedback}
        return render_to_response('feedback/view_feedback.html', context,
                                  context_instance=RequestContext(request))


class AnonymousFeedbackAdmin(admin.ModelAdmin):
    list_display = ['user', 'message', 'time', 'type', 'view']
    search_fields = ['user', 'message']
    list_filter = ['type', 'time']

    def view(self, obj):
        return "<a href='%s'>View</a>" % obj.get_absolute_url()

    view.allow_tags = True

    def get_urls(self):
        urls = super(AnonymousFeedbackAdmin, self).get_urls()
        my_urls = patterns('',
            url(r'^view/(?P<feedback_id>\d+)/$',
                self.admin_site.admin_view(self.view_feedback),
                name='view-anon-feedback'),
        )
        return my_urls + urls

    def view_feedback(self, request, feedback_id):
        feedback = get_object_or_404(AnonymousFeedback, id=feedback_id)
        context = {'feedback': feedback}
        return render_to_response('feedback/view_feedback.html', context,
                                  context_instance=RequestContext(request))


admin.site.register(Feedback, FeedbackAdmin)
if getattr(settings, 'ALLOW_ANONYMOUS_FEEDBACK', False):
    admin.site.register(AnonymousFeedback, AnonymousFeedbackAdmin)
admin.site.index_template = 'feedback/index.html'
