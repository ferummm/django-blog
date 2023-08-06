from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.shortcuts import redirect 
from django.urls import reverse

class ArticleView(View):
    template_name="articles/index.html"
    def get(self, request):
        return redirect(reverse('article', kwargs={'tags': 'python', 'article_id': 42}))


def index(request, tags, article_id):
    return render(request, 'articles/index.html', context={'tags': tags, 'article_id': article_id})
    
