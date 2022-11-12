from django.shortcuts import render, get_object_or_404
from .models import ProjectBlog


# Create your views here.
def all_blogs(request):
    all_blogs = ProjectBlog.objects.order_by('-date')
    return render(request, 'blog/all_blogs.html',{'data':all_blogs})

def detail(request,blog_id):
    blog = get_object_or_404(ProjectBlog,pk=blog_id)
    return render(request, 'blog/detail.html',{'blog':blog})
