from django.shortcuts import render
from blob.models import Post # <==

# мой проект/blob/views.py
def post_list(request):
    posts = Post.objects.all()# <==
    return render(request,
                  'blob/post_list.html',
                  {'posteki':posts})# <==
def post_detail(request, pk):
    post = Post.objects.get(id=pk)# <==
    return render(request,
                  'blob/post_detail.html',
                  {'post':post})# <==
