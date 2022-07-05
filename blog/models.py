from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import datetime
from django.core import validators
from django.urls import reverse
from django.http import HttpResponse

'''
django form validation
https://pythonguides.com/django-form-validation/
'''
'''
https://www.geeksforgeeks.org/django-rest-api-crud-with-drf/
Django Form - How to create a custom form template with a loop for one field?
https://django.fun/qa/26007/

todooooooooooooooooooooooooooooooooooooooooo

Python Project – Create a Calorie Calculator in Django
https://prutor.ai/python-django-calorie-calculator/


https://legionscript.medium.com/building-a-food-delivery-app-with-django-and-python-3-part-2-building-the-ordering-system-part-1-902fb69fdc88

https://legionscript.medium.com/building-a-food-delivery-app-with-django-and-python-3-part-2-building-the-ordering-system-part-1-902fb69fdc88

https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Models

https://djangobook.com/django-tutorials/mastering-django-advanced-models/

beginning django
https://www.webforefront.com/django/setuprelationshipsdjangomodels.html

https://zerotobyte.com/django-many-to-many-relationship-explained/
Django reverse_lazy() function
https://zerotobyte.com/django-reverse-url-reverse-function/
'''


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=80)

    def __str__(self):
        return self.name


class Blog(models.Model):
    '''
    add slug
    '''
    title = models.CharField(max_length=70, verbose_name='Title', unique=True,
                             validators=[validators.MaxLengthValidator(100), validators.MinLengthValidator(2)])
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    pic = models.FileField(upload_to='blog_imgs/')
    categories = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('detail', kwargs={'pk': self.pk})


'''
class Category(models.Model):
    title = models.CharField(max_length=55)

    class Meta:
        verbose_name = 'Food Category'
        verbose_name_plural = 'Food Categories'

    def __str__(self):
        return self.title

class FoodItem(TimeStampWithCreator):
    CATEGORY_CHOICES = (
        ('takeway', 'Takeaway'),
        ('dine_in', 'Dine In'),
        ('function', 'Function'),
    )
    type_menu_select = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='takeway')
    category = models.ForeignKey(FoodCategory, on_delete=models.CASCADE)


sort by date
last comment. 
'''


class Comment(models.Model):
    name = models.CharField(max_length=70)
    text = models.TextField()
    comment_date = models.DateTimeField(auto_now_add=True)
    blogs = models.ForeignKey(Blog, related_name='comments', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


def sendEmail(request):
    time = datetime.datetime.now()
    msg = f'Hello time now is {time}'
    return HttpResponse(msg, content_type='text/plain')


'''
https://stackoverflow.com/questions/53412687/django-i-want-to-sort-posts-by-last-comment-update

class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.DO_NOTHING,)
    title = models.CharField(max_length=200)
    text = RichTextUploadingField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    updated_date = models.DateTimeField(blank=True, null=True)


    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey('blog.Post', related_name='comments', on_delete=models.DO_NOTHING,)
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        Post.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return self.text

def approved_comments(self):
    return self.comments.filter(approved_comment=True)


def post_list(request):
    posts = post.objects.filter(updated_date__lte=timezone.now()).order_by('-updated_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

blog.views.post_detail


@login_required
def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('post_detail', pk=pk)

def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'blog/add_comment_to_post.html', {'form': form})


@login_required
def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('post_detail', pk=comment.post.pk)


Post.objects.filter(comments__approved_comment=True).annotate(max_activity=Max('comments__created_date')).order_by('max_activity', 'updated_date')
FYI approved_comments and approve method inside Comment model class won't work. They should be like this:

def approved_comments(self):
    return self.__class__.objects.filter(approved_comment=True)

def approve(self):
    self.approved_comment = True
    self.post.updated_date = timezone.now()
    self.post.save()
    self.save()
'''
