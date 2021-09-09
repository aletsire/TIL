from django.db import models

from imagekit.models import ProcessedImageField
from imagekit.processors import Thumbnail

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    # image = models.ImageField(blank=True)
    image_thumb = ProcessedImageField(
        blank=True,
        processors=[Thumbnail(200, 200)],
        format='JPEG',
        options={'quality': 90}
    ) # 썸네일 이미지를 만듦 (원본 이미지를 가공하여 넣기 때문에 원본은 저장 X, 썸네일만 저장)


    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title