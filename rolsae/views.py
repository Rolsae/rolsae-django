from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post, Question, Choice
# Create your views here.

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'rolsae/post_list.html', {'posts': posts})

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'rolsae/post-detail.html', {'post': post})
