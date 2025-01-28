from django.shortcuts import render ,get_object_or_404, redirect
from django.contrib.auth.forms import UserCreationForm
from .models import BlogPost, LikeDislike
from .forms import BlogPostForm

# Create your views here.
# forms -> views -> templates -> urls
def dashboard(request):
    if request.method == "POST":
        form = BlogPostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = BlogPostForm()
    blogs = BlogPost.objects.all()
    return render(request, 'dashboard.html', {'blogs': blogs, 'form': form})

def upload_post(request):
    if request.method == "POST":
        form = BlogPostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('dashboard')
    else:
        form = BlogPostForm()
    
    return render(request, 'upload_post.html', {'form': form}) 
    
def edit_post(request, post_id):
    post = get_object_or_404(BlogPost, id = post_id)
    if post.author != request.user:
        return redirect('dashboard')
    if request.method == "POST":
        form = BlogPostForm(request.POST, instance = post)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = BlogPostForm(instance=post)

    return render(request, 'edit_post.html', {'form': form, 'post': post})

def delete_post(request, post_id):
    post = get_object_or_404(BlogPost, id = post_id)
    post.delete()
    return redirect('dashboard')

def like_post(request, post_id):
    post = get_object_or_404(BlogPost, id = post_id)
    like_dislike, created = LikeDislike.objects.get_or_create(user=request.user, post=post)
    if not created:
        like_dislike.is_like = True
        post.save()
    return redirect('dashboard')

def dislike_post(request, post_id):
    post = get_object_or_404(BlogPost, id = post_id)
    like_dislike, created = LikeDislike.objects.get_or_create(user=request.user, post=post)
    if not created:
        like_dislike.is_like = False
        post.save()
    return redirect('dashboard')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    
    return render(request, 'signup.html', {'form': form})

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    
    return render(request, 'signup.html', {'form': form})

def my_posts(request):
    posts = BlogPost.objects.filter(author=request.user)
    return render(request, 'my_posts.html', {'posts': posts})


