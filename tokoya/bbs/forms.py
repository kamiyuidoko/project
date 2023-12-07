from django import forms
from . models import TopicModel,ViewModel,GenreModel

class TopicCreateForm(forms.ModelForm):
    class Meta:
        model = TopicModel
        fields = ('name','title','detail','genre')
        labels={
            'name':'作成者',
            'title':'タイトル',
            'detail':'詳細',
            'genre':'ジャンル',
        }

    def __init__(self, *args, **kwargs):
        super(TopicCreateForm, self).__init__(*args, **kwargs)

        # 各フィールドの help_text を非表示にする
        for field_name in self.fields:
            self.fields[field_name].help_text = None

class ReplyForm(forms.ModelForm):
    class Meta:
        model = ViewModel
        fields = ('name','text')
        labels = {
            'name':'ユーザ名',
            'text':'返信',
        }

    def __init__(self,*args,**kwargs):
        super(ReplyForm,self).__init__(*args,**kwargs)

        for field_name in self.fields:
            self.fields[field_name].help_text = None