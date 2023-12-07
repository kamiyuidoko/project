from django.contrib import admin
from .models import TopicModel,GenreModel,ViewModel

# Register your models here.

admin.site.register(TopicModel)
admin.site.register(GenreModel)
admin.site.register(ViewModel)

