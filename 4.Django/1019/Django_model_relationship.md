# Django Model Relationship



### 1. 회원가입

```python
# views.py
from . forms import CustomUserCreationForm

def signup(request):
    if request.method == "POST": # 사용자가 값을 입력했을때
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts:login')
    else: #GET일 때 => url에 접속했을때
        form = CustomUserCreationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/signup.html', context)


# html
{% extends 'base.html' %}
{% block content %}
<h2>Sign up</h2>

<form action="" method="POST">
    {% csrf_token %}
    {{ form.as_p }}
    <button>Signup!</button>

</form>

{% endblock content %}
```

![image-20211019103901744](1019_workshop.assets/image-20211019103901744.png)															



### 2. 로그인

```python
# views.py
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user() # form에서 어떤 유져인지 가져오기
            auth_login(request, user)
            return redirect('todos:index')
    else:
        form = AuthenticationForm()

    context = {
        'form': form,
    }
    return render(request, 'accounts/login.html', context)


# html
{% extends 'base.html' %}

{% block content %}
<h2>Login</h2>
<form action="" method="POST">
  {% csrf_token %}
  {{form.as_p}}
  <button>login</button>

</form>

<a href="{% url 'accounts:signup' %}">Signup</a>
{% endblock content %}
```

![image-20211019104110368](1019_workshop.assets/image-20211019104110368.png)

​																							



### 3. Todo 목록

```python
# views.py
from django.contrib.auth.decorators import login_required
@login_required
def index(request):
    # 현재는 모든 사용자의 것을 볼 수 있음
    # todos = Todo.objects.all()

    # 본인이 작성한 todo만 보이게
    todos = request.user.todo_set.all()

    context = {
        'todos': todos,
    }
    return render(request, 'todos/index.html', context)


# html
{% extends 'base.html' %}
{% block content %}
<h1>todo index</h1>

{% for todo in todos %}
    <div>
        <h1>할 일: {{todo.title}}</h1>
        <p>작성자: {{todo.author}}</p>
        <p>완료여부: {{todo.completed}}</p>
        <hr>
    </div>
{% endfor %}

{% endblock content %}
```

![image-20211019104352225](1019_workshop.assets/image-20211019104352225.png)

### 4. Todo 생성

```python
# views.py
from django.contrib.auth.decorators import login_required
from .forms import TodoForm
@login_required
def new(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.author = request.user
            todo.save()
            return redirect('todos:index')
    else:
        form = TodoForm()
    context = {
        'form': form
    }
    return render(request, 'todos/new.html', context)


# html
{% extends 'base.html' %}
{% block content %}
    <h1>NEW</h1>
    <form action="" method="POST">
    {% csrf_token %}
    {{form.as_p}}
    <button>NEW</button>
    </form>

{% endblock content %}
```

![image-20211019104613367](1019_workshop.assets/image-20211019104613367.png)
