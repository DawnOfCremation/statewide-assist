from django.shortcuts import render, get_object_or_404


from .models import Blog
# Create your views here.
def allblogs(request):
    blogs = Blog.objects
    return render(request, 'blog/allblogs.html', {'blogs': blogs})

def detail(request, blog_id):
    detailblog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/detail.html', {'blog':detailblog})

#def nextBlog(request, blog_id):
#    nextblogNum = blog_id + 1
#    detailblog = get_object_or_404(Blog, pk=nextblogNum )
#    return render(request, 'blog/detail.html', {'blog':detailblog})
#<!--<a href="{% url 'nextblog' blog.id %}" class="text-right">Next ></a>-->
#
