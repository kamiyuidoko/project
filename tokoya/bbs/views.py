from django.shortcuts import render, get_object_or_404,redirect
from .models import TopicModel,GenreModel,ViewModel
from .forms import TopicCreateForm,ReplyForm
from django.utils import timezone
from django.http import HttpResponseRedirect,HttpResponse


# Create your views here.

def homeView(request):
    topic = TopicModel.objects.all()
    genre = GenreModel.objects.all()

    return render(request,'bbs/home.html',{'topic':topic,'genre':genre})

def view(request,data):
    genre = get_object_or_404(GenreModel, genre=data)
    topic = TopicModel.objects.filter(genre=genre)

    form = ReplyForm()

    context = {
        'data' : data,
        'topic' : topic,
        'ReplyForm' : form,
    }

    return render(request,'bbs/view.html',context)

def view_detail(request,pk):
    if request.method == 'POST':
        form = ReplyForm(request.POST)
        if form.is_valid():
            reply_instance = form.save(commit=False)
            reply_instance.date = timezone.now()
            topic = get_object_or_404(TopicModel,pk=pk)
            reply_instance.topic = topic
            reply_instance.save()

            topic = get_object_or_404(TopicModel,pk=pk)
            reply = ViewModel.objects.filter(topic=topic)
            form = ReplyForm()
            
            context = {
                'topic':topic,
                'reply':reply,
                'ReplyForm':form,
                }

            return render(request,'bbs/view_detail.html',context)
    else:
        form = ReplyForm()

    topic = get_object_or_404(TopicModel,pk=pk)
    reply = ViewModel.objects.filter(topic=topic)

    form = ReplyForm()

    context = {
        'topic':topic,
        'reply':reply,
        'ReplyForm':form,
    }
    return render(request,'bbs/view_detail.html',context)

    
def topic_create(request):
    form = TopicCreateForm()

    context = {
        'TopicCreateForm':form,
    }
    return render(request,'bbs/topic_create.html',context)

def addTopic(request):
    if request.method == 'POST':
        form = TopicCreateForm(request.POST)
        if form.is_valid():
            # コミットを保留し、dateフィールドを手動で設定
            topic_instance = form.save(commit=False)
            topic_instance.date = timezone.now()
            topic_instance.save()
            return redirect('homeViews')
    else:
        form = TopicCreateForm()

    topic = TopicModel.objects.all()
    genre = GenreModel.objects.all()

    return render(request,'bbs/home.html',{'topic':topic,'genre':genre,'TopicCreateForm':form})

def rule(request):
    return render(request,'bbs/rule.html')

def mysite(request):
    return render(request,'bbs/mysite.html')

