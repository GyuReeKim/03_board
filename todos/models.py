from django.db import models

# Create your models here.
# 데이터를 저장하는 구조 만들기
class Todo(models.Model):
    # 제목
    title = models.CharField(max_length=50)
    # 상세내용
    content = models.CharField(max_length=200)
    # 마감일
    due_date = models.DateField()