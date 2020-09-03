from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post

def index(request):
    # return HttpResponse('Hello World! このページは投稿のインデックスです。')
    posts = Post.objects.order_by('-published')
    return render(request, 'posts/index.html', {'posts': posts})

def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'posts/post_detail.html', {'post': post})

def about(request):
    return render(request, 'posts/about.html')

# Create your views here.
# Django2.0以降ではURLをよりシンプルに定義できるpathが追加されている
# from django.urls import poth
# urlpatterns = [
#    path('admin/', admin.site.urls),
#    path(URLパターン, ビュー関数),...
# ]