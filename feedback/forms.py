from django import forms

from feedback.models import Feedback, AnonymousFeedback

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        exclude = ('user',)


class AnonymousFeedbackForm(forms.ModelForm):
    class Meta:
        model = AnonymousFeedback
        exclude = ('user',)

