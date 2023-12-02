from django.shortcuts import render, redirect
from .models import Post

# Create your views here.
def posts_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/PostList.html', {'posts': posts})


def post_like(request):
    if request.method == 'POST':
        post_id = int(request.POST['post_id'])
        post = Post.objects.get(id=post_id)  #  получаем объект
        post.likes += 1  # изменяем поле name
        post.save()
        return redirect('posts_list')
