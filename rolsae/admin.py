from django.contrib import admin
from .models import Post
from .models import Question
# Register your models here.
admin.site.register(Post)
admin.site.register(Question)
