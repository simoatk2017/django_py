from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from .forms import BlogForm, CommentForm
from django.contrib.auth.decorators import login_required
from .models import Blog, Category
from django.contrib import messages
from django.db.models import Q
import datetime


# Create your views here.
# decoration
# @login_required

def greeting(request):
    date = datetime.datetime.now()
    msg = f'Hello from Django {date}'
    return HttpResponse(msg, content_type='text/html')





@login_required
def addpost(request):
    form = BlogForm()
    if request.method == 'POST':
        print(request.user)
        form = BlogForm(request.POST)
        if form.is_valid():
            form.save(commit=False)
            form.instance.author = request.user
            form.save()
            redirect('/posts')

    return render(request, 'blog/add_blog.html', {'form': form})


from .filters import BlogFilter



def getposts(request):

    '''

    :param request:
    :return:
    '''
    error = False
    message = ''
    template_name = 'blog/blog_new.html'
    articles = Blog.objects.all().order_by('-title')
    # if 'queryBooks' in request.GET:
    myFilter = BlogFilter(request.GET, queryset=articles)
    articles = myFilter.qs
    print('My_filter ', myFilter)
    context = {
        'articles': articles,
        'myFilter': myFilter,
        'date': datetime.datetime.now()
    }

    return render(request, template_name, context)


def detail_posts(request, pk):
    form = CommentForm()
    try:
        post = Blog.objects.get(pk=pk)
    except Blog.DoesNotExist:
        # raise Http404('Resources Not Found')
        return render(request, '404.html')
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save(commit=False)
            form.instance.blogs = post
            form.save()
            redirect(f'detail/{pk}')
            # add message

    return render(request, 'blog/detail.html', {'post': post, 'form': form})
