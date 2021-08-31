from django.urls import path
from . import views

app_name = 'articles'
urlpatterns = [
    path('index/', views.index),
    path('greeting/', views.greeting),
    path('dinner/', views.dinner),
    path('image/', views.image),
    path('template_language/', views.template_language),
    path('throw/', views.throw),
    path('catch/', views.catch),
    path('hello/<name>/', views.hello),
    # path('hello/<str:name>/', views.hello)
]
