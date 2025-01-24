from django.shortcuts import render ,get_object_or_404, redirect
from .models import BlogPost
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
    blog = BlogPost.objects.all()
    return render(request, 'dashboard.html', {'blogs': blog, 'form': form})

def upload_post(request):
    if request.method == "POST":
        form = BlogPostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = BlogPostForm()
    
    return render(request, 'upload_post.html', {'form': form}) 
    
def edit_post(request, post_id):
    post = get_object_or_404(BlogPost, id = post_id)
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
    post.likes += 1
    post.save()
    return redirect('dashboard')

def dislike_post(request, post_id):
    post = get_object_or_404(BlogPost, id = post_id)
    post.dislikes += 1
    post.save()
    return redirect('dashboard')




