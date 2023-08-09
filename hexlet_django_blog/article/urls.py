from django.urls import path

from hexlet_django_blog.article import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='articles_index'),
    path('<int:id>/edit/', views.ArticleFormEditView.as_view(), name='article_update'),
    path('<int:article_id>/', views.ArticleView.as_view(), name='the_article'),
    #path('<str:tags>/<int:article_id>/', views.index, name='article'),
    path('create/', views.ArticleFormCreateView.as_view(), name='article_create'),
    path('<int:id>/delete/', views.ArticleFormDeleteView.as_view(), name='article_delete'),
]