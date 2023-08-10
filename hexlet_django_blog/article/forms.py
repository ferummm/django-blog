from django import forms 
from django.forms import ModelForm
from .models import Article, Comment

class CommentArticleForm(forms.Form):
    content = forms.CharField(label='Комментарий')

class ArticleCommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['content']

class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ['name', 'body']