from django import forms
from blog.models import Post, Comment
from django.core.urlresolvers import reverse


class NewBlog(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'public']


class UpdateBlog(forms.ModelForm):
    update = True

    class Meta:
        model = Post
        exclude = ['author']


class NewComment(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content', 'post']