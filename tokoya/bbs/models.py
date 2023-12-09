from django.db import models
from django.urls import reverse

# Create your models here.

class GenreModel(models.Model):
    genre = models.CharField(max_length=30,help_text="ジャンル")

    def __str__(self):
        return self.genre

class TopicModel(models.Model):
    name = models.CharField(max_length=16,help_text="作成者")
    title = models.CharField(max_length=32,help_text="タイトル")
    detail = models.CharField(max_length=100,help_text="詳細")
    genre = models.ForeignKey(GenreModel,on_delete=models.CASCADE)
    date = models.DateTimeField(help_text="作成日")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('bbs:view', kwargs={'pk': self.pk}) 


class ViewModel(models.Model):
    name = models.CharField(max_length=16,help_text="返信者")
    text = models.CharField(max_length=200,help_text="返信")
    date = models.DateTimeField(help_text="投稿日")
    topic = models.ForeignKey(TopicModel,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.text
