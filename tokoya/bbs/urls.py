from django.urls import path
from . import views

urlpatterns = [
    path('',views.homeView,name='homeViews'),
    path('view/<str:data>/',views.view,name='view'),
    path('topic/',views.topic_create,name='topic_create'),
    path('add/',views.addTopic,name='addTopic'),
    path('view_detail/<int:pk>/',views.view_detail,name = 'view_detail'),
    path('rule/',views.rule,name='rule'),
    path('mysite/',views.mysite,name='mysite'),
]