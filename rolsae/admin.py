from django.contrib import admin
from .models import Post
from .models import Question
from django_summernote.admin import SummernoteModelAdmin
# Register your models here.
admin.site.register(Post)
admin.site.register(Question)
