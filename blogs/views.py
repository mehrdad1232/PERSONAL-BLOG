from django.shortcuts import redirect, render
from .models import Blog, Category, Comment
from django.shortcuts import get_object_or_404
from django.db.models import Q
from django.http import HttpResponseRedirect

def post_by_category(request, category_id):
    posts = Blog.objects.filter(status=1 ,category=category_id)
    category = get_object_or_404(Category, pk=category_id)
    context = {
        "posts":posts,
        "category":category,
    }
    return render(request, "post_by_category.html", context)

def blog(request, slug):
    single_blog = get_object_or_404(Blog, slug=slug, status=1)
    if request.method == 'POST':
        comment = Comment()
        comment.user = request.user
        comment.blog = single_blog
        comment.comment = request.POST['comment']
        comment.save()
        return HttpResponseRedirect(request.path_info)
        
    
    #comment
    comments = Comment.objects.filter(blog=single_blog)
    comment_counter = comments.count()
    context = {
        "single_blog":single_blog,
        "comments":comments,
        "comment_counter":comment_counter,
    }
    return render(request, "blogs.html", context)

def search(request):
    keyword = request.GET.get('keyword')
    blogs = Blog.objects.filter(Q(title__icontains=keyword) | Q(short_description__icontains=keyword) |  Q(blog_body__icontains=keyword), status =1)
    
    context ={
        "blogs":blogs,
        "keyword":keyword,
    }
    return render(request, "search.html", context)