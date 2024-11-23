from django.http import HttpResponse
from django.shortcuts import render
from .models import Article
from django.views import generic

# Create your views here.

class HomeView(generic.TemplateView):
    template_name = 'index.html'


class ArticleView(generic.DetailView):
    model = Article
    template_name = 'article_view.html'


class AboutView(generic.TemplateView):
    template_name = 'about_view.html'


from django.views import generic
from .models import Article

class ArticleList(generic.ListView):
    model = Article 
    queryset = Article.objects.filter(is_published=True) 
    ordering = ['-created_date']
    context_object_name = 'articles'
    template_name = 'index.html'
    paginate_by = 10


