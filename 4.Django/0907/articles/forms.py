from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    
    class Meta:
        model = Article
        fields = '__all__'
        # fields = ['title', 'content'] -> 권장
        # fields = ('title', 'content')
        # exclude = ('title',) -> title빼고
        # 참고로 ('title') -> 문자열 / ('title')=='title'로 쓰려면 ,가 필수