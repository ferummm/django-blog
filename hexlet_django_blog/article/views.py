from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views import View
from django.shortcuts import redirect 
from django.urls import reverse

from .models import Article
from .forms import ArticleForm

from django.contrib import messages


class IndexView(View):

    template_name="articles/index.html"

    def get(self, request, *args, **kwargs):
        articles = Article.objects.all()[:15]
        return render(request, 'articles/index.html', context={
            'articles': articles,
        })

class ArticleView(View):

    def get(self, request, *args, **kwargs):
        article = get_object_or_404(Article, id=kwargs['article_id'])
        messages.get_messages(request)
        return render(request, 'articles/show.html', context={
            'article': article
        })

class ArticleFormEditView(View):

    def get(self, request, *args, **kwargs):
        article_id = kwargs.get('id')
        article = Article.objects.get(id=article_id)
        form = ArticleForm(instance=article)
        return render(request, 'articles/update.html', {'form': form, 'article_id':article_id})
    
    def post(self, request, *args, **kwargs):
        article_id = kwargs.get('id')
        article = Article.objects.get(id=article_id)
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            messages.add_message(request, messages.SUCCESS, 'Article updated successfully')
            form.save()
            return redirect('/articles')
        return render(request, 'articles/update.html', {'form': form, 'article_id': article_id})

class ArticleFormCreateView(View):
    
    def get(self, request, *args, **kwargs):
        form = ArticleForm()
        return render(request, 'articles/create.html', {'form': form})
    
    def post(self, request, *args, **kwargs):
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            #messages.add_message(request, messages.SUCCESS, 'Article added successfully')
            messages.success(request, 'Article added successfully')
            return redirect('articles_index') 
        return render(request, 'articles/create.html', {'form': form})

class ArticleFormDeleteView(View):

    def post(self, request, *args, **kwargs):
        article_id = kwargs.get('id')
        article = Article.objects.get(id=article_id)
        if article:
            article.delete()
            messages.success(request, 'Article deleted successfully')
        else:
            messages.error(request, "Failed to find the article to delete")
        return redirect('articles_index')

def index(request, tags, article_id):
    return render(request, 'articles/index.html', context={'tags': tags, 'article_id': article_id})
    
"""class ArticleCommentFormView(View):

    def post(self, request, *args, **kwargs):
        form = ArticleCommentForm(request.POST) 
        if form.is_valid(): 
            form.save() 
            comment = form.save(commit=False) # Получаем заполненную модель
            # Дополнительно обрабатываем модель
            comment.content = check_for_spam(form.data['content'])
            comment.save()

class ArticleCommentsView(View):

    def get(self, request, *args, **kwargs):
        comment = get_object_or_404(Comment, id=kwargs['id'], article__id=kwargs['article_id'])

        return render( ... ) """
