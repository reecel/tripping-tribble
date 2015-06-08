from django import forms

from .models import Post, Critique

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)

class CritiqueForm(forms.ModelForm):

    class Meta:
        model = Critique
        fields = ('author', 'text',)
