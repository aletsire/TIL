from django.shortcuts import render, redirect
from django.contrib import messages
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

            # add_message
            # messages.add_message(request, messages.INFO, '게시글 작성 성공')

            # shortcut
            messages.info(request, '게시글작성')


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

    # messages.add_massage(request, messages.ERROR, '게시글이 삭제?')
    messages.error(request, '게시글 삭제')

    return redirect('articles:index')


def update(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES, instance=article)
        if form.is_valid():
            article = form.save()
            # messages.add_massage(request, messages.WARNING, '게시글이 수정')
            messages.warning(request, '게시글 수정')
            return redirect('articles:detail', article.pk)

    else:
        form = ArticleForm(instance=article)

    context = {
        'article': article, # article.pk를 a태그에 사용하려고
        'form': form,
    }
    return render(request, 'articles/update.html', context)