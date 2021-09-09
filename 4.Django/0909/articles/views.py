from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods
from .models import Article
from .forms import ArticleForm

# Create your views here.

def index(request):
    articles = Article.objects.order_by('-id') # orm으로 순서 변경
    context = {
        'articles': articles
    }
    return render(request, 'articles/index.html', context)

@require_http_methods(['GET', 'POST'])
def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES) # data= 생략가능
        if form.is_valid():
            form.save()
            return redirect('articles:index')

    
    else: 
        form = ArticleForm()
    context = { 
        'form': form
    }
    return render(request, 'articles/create.html', context)

def detail(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article': article,
    }
    return render(request, 'articles/detail.html', context)

def delete(request, pk):
    article = Article.objects.get(pk=pk)
    article.delete()
    return redirect('articles:index')


def update(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES, instance=article)
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', article.pk)

    else:
        form = ArticleForm(instance=article)

    context = {
        'article': article, # article.pk를 a태그에 사용하려고
        'form': form,
    }
    return render(request, 'articles/update.html', context)