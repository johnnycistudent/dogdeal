from django import forms
from .models import ProductWanted, Comment

class AddCommentForm(forms.ModelForm):
    
    
    class Meta:
        model = Comment
        fields = ('comment',)