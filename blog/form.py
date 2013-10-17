from django import forms
from blog.models import Post, Comment


class NewBlog(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']


class NewComment(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content', 'post']