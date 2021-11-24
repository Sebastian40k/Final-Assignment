from django import forms
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

from . models import Comment, Post

class EmailPostForm(forms.Form):
    name = forms.CharField(max_length=25)
    email = forms.EmailField()
    to = forms.EmailField()
    comments = forms.CharField(required=False,
                               widget=forms.Textarea)

#@login_required
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')


class SearchForm(forms.Form):
    query = forms.CharField()


class NewPost(forms.Form):
    class Meta:
        model = Post
        fields = ('Title','slug','author','body')