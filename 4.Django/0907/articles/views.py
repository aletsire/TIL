
from django.views.decorators.http import require_http_methods
from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm
# Create your views here.

def index(request):
    articles = Article.objects.all()[::-1]
    context = {
        'articles': articles
    }
    return render(request, 'articles/index.html', context)

@require_http_methods(['GET', 'POST'])
def create(request):
    # 5. create경로로 요청이 들어옴(POST) [case1. 잘못된 입력]
    # 10. create 경로로 요청이 들어옴(POST) [case2. 올바른 입력]
    if request.method == 'POST':
        # 6. 데이터가 입력된 종이를 가져옴 -> ArticleForm을 인스턴스(빈종이 +사용자 데이터)
        # 11. 데이터가 입력된 종이를 가져옴 -> ArticleForm을 인스턴스(빈종이 +사용자 데이터)
        form = ArticleForm(data=request.POST) # data= 생략가능
        # 7. 사용자가 입력한 데이터가 유효한지 확인
        # 12. 사용자가 입력한 데이터가 유효한지 확인
        if form.is_valid():
            # 13. 데이터를 db에 저장한다.
            form.save()
            # 14. index로 리다이렉트 시켜준다
            return redirect('articles:index')

    
    else: # 1. create 경로로 요청이 들어옴(GET-DB에 영향 X)-> 빈종이(Form) 응답
        form = ArticleForm() # 2. ArticleForm으로 빈 종이 생성(인스턴스 생성)


    # 3. 사용자에게 빈 종이를 주기 위해서context에 form을 담는다
    # 8. 잘못도니 데이터를 다시 입력
    context = { 
        'form': form
    }

    # 4. 사용자에게 데이터를 받기 위해 빈 종이를 넘겨준다.
    # 9. 사용자에게 올바른 데이터를 받기 위해 form을 넘겨준다.
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
        form = ArticleForm(request.POST, instance=article)
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