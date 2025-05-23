from django import forms
from django.forms import ModelForm
from tweet.models import Tweet

class AddTweetForm(forms.Form):
    Username = forms.CharField(max_length=50, label='Username')
    Tweet = forms.CharField(max_length=280, label='Tweet', widget=forms.Textarea(attrs={'rows': 3, 'cols': 30}))

class AddTweetModelForm(ModelForm):
    class Meta:
        model = Tweet
        fields = ['user', 'tweet']
        widgets = {
            'user': forms.TextInput(attrs={'placeholder': 'Enter your Username'}),
            'tweet': forms.Textarea(attrs={'placeholder': 'Enter your Tweet', 'rows': 3, 'cols': 30}),
        }