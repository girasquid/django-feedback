from django import forms
from models import Feedback

class FeedbackForm(forms.ModelForm):
    
    class Meta:
        
        model = Feedback
        
    def __init__(self, *args, **kwargs):
        super(FeedbackForm, self).__init__(*args, **kwargs)
        self.fields['user'].widget = forms.HiddenInput()