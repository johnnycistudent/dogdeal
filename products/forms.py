from django import forms
from .models import ProductSelling, ProductWanted, Comment


class AddSaleAdForm(forms.ModelForm):
    
    
    class Meta:
        model = ProductSelling
        fields = ('title', 'description', 'price', 'breed', 'gender', 'image', 'color', 'location', 'status',)

class AddWantedAdForm(forms.ModelForm):

    class Meta:
        model = ProductWanted
        fields = ('title', 'description', 'price', 'breed', 'gender', 'color', 'location', 'status',)

class AddCommentForm(forms.ModelForm):
    
    
    class Meta:
        model = Comment
        fields = ('comment',)