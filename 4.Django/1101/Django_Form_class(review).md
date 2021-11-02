# Django Form Class

## Form

- Form은 데이터 손상에 대한 중요한 방어수단
- 주요 처리 기능
  1. 렌더링을 위한 데이터 준비 및 재구성
  2. 데이터에 대한 HTML forms 생성
  3. 클라이언트로부터 받은 데이터 수신 및 처리



#### Django 'Form Class'

- form 내 field, fields 배치, 디스플레이 widget, label, 초기값, 유효하지 않은 field에 관련된 여러 메세지를 결정
- Django는 사용자의 데이터를 받아야할 작업(데이터 유효성 검증, 필요시 입력된 데이터 검증 결과 재출력, 유효한 데이터에 대해 요구되는 동작 수행 등)과 반복 코드를 줄여 줌



#### Form 선언 예시

```python
# fomrs.py
from django import forms

class ArticleForm(forms.Form):
    title = forms.CharField(max_length=10)
    content = forms.CharField()
```

```python
# views.py
from .fomrs import ArticleForm

def new(request):
    form = ArticleForm()
    context = {
        'form': form,
    }
    return render(request, 'articles/new.html', context)
```



### Form rendering options

1. as_p()
   - 각 필드가 `p`태그로 감싸져서 렌더링 됨

2. as_ul()
   - 각 필드가 `li`태그로 감싸져서 렌더링 됨
   - `ul`태그는 직접 작성해야 함
3. as_table()
   - 각 필드가 `tr`태그로 감싸져서 렌더링 됨
   - `table`태그는 직접 작성해야 함



### Django의 HTML input 요소 표현 방법 2가지

1. Form fields
   - input에 대한 유효성 검사 로직을 처리하여 템플릿에서 직접 사용 됨
2. Widgets
   - 웹 페이지의 HTML input 요소 렌더링
   - GET/POST 딕셔너리에서 데이터 추출
   - 하지만 widgets은 반드시 form fields에 할당 됨

#### Widgets

- Django의 HTML input element 표현
- HTML 렌더링을 처리
- 주의
  - Form Fields와 혼동되어서는 안됨
  - Form Fields는 input 유효성 검사를 처리

```python
# forms.py
from django import forms

class ArticleForm(forms.Form):
    title = forms.CharField(max_length=10)
    content = forms.CharField(widget=forms.Textarea)
```





## ModelForm

- Model을 통해 Form Class를 만들 수 있는 Helper
- 일반 Form Class와 같은 방식(객체 생성)으로 view에서 사용 가능



#### ModelForm 예시

```python
# forms.py
from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = '__all__'
        # exclude = ('title',)
```

```python
# views.py
def create(request):
    form = ArticleForm(request.POST)
    if form.is_valid():
        article = form.save()
        return redirect('articles:detail', article.pk)
    return redirect('articles:new')
```



#### is_valid()

- 유효성 검사를 실행하고 데이터가 유효한지 여부를 boolean으로 반환



#### save()

```python
# create a form instance form Post data
form = ArticleForm(request.POST)

# CREATE
# save a new Article object from the form's data
new_article = f.save()

# UPDATE
# Create a form to edit an existing Ariticle, but POST data to populate the form
article = Article.objects.get(pk=1)
form = ArticleForm(request.POST, instance=article)
form.save()
```

  

#### Create view 함수 구조 변경 예시

```python
def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm()
    context = {
        'form': form,
    }
    return render(request, 'articles/create.html', context)
```

#### Delete view 함수 구조 변경 예시

```python
def delete(request):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        article.delete()
        return redirect('articles:index')
    return redirect('articles:detail', article.pk)
```

#### Update view 함수 구조 변경 예시

```python
def update(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.user == article.user:
        if request.method == 'POST':
            form = ArticleForm(request.POST, instance=article)
            if form.is_valid():
                form.save()
                return redirect('articles:detail', article.pk)
        else:
            form = ArticleForm(instance=article)
    else:
        return redirect('articles:index')
    context = {
        'form': form,
        'article': article,
    }
    return render(request, 'articles/update.html', context)
```

