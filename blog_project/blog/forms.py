from django import forms

from .models import Post, Comment


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('author','title', 'text',)

        widgets = {
            'title': forms.TextInput(attrs={'class': 'textinputclass'}),
            'text': forms.Textarea(attrs={'class': 'editable medium-editor-textarea postcontent'}),
        }


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('Name', 'Comment',)

        widgets = {
            'Name': forms.TextInput(attrs={'class': 'textinputclass'}),
            'Comment': forms.Textarea(attrs={'class': 'editable medium-editor-textarea'}),
        }
