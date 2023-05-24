from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import PostForm
from .models import Post


# Create your views here.
# @login_required
def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False) #바로 저장하지 않는다
            #post.user = request.user
            post.save()
            messages.success(request, "포스팅 저장 완료")
            return redirect(post)
    else:
        form = PostForm()

    return render(request, "post_form.html",{
        "form" : form,
    })

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, "post_detail.html", {
        "post" : post,
    })

def post_list(request):
    postList = Post.objects.all()
    return render(request, 'post_list.html', {
        "postList" : postList
    })