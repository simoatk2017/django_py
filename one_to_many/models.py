from django.db import models


# Create your models here.
class Author1(models.Model):
    name = models.CharField(max_length=255)
    age = models.PositiveIntegerField()

    def __str__(self):
        return self.name

    class Meta:
        db_table = "authorss"
        verbose_name = "Authorss"
        verbose_name_plural = "Authorss"

'''
class Post(models.Model):
    # ... fields ...

class Comment(models.Model):
    # ... fields ...
    post = models.ForeignKey(Post, related_name=???)
1. Don't specify related_name
If you don't specify a name, django will create one by default for you.

some_post = Post.objects.get(id=12345)
comments = some_post.comment_set.all()
2
2. Specify a custom value
Usually you want to specify something to make it more natural. For example, 
related_name="comments".

some_post = Post.objects.get(id=12345)
comments = some_post.comments.all()


. Prevent the reverse reference from being created
Sometimes you don't want to add the reference to the foreign model, so use related_name="+" to not create it.

some_post = Post.objects.get(id=12345)
comments = some_post.comment_set.all() # <-- error, no way to access directly
related_query_name is basically the same idea, but when using filter() on a queryset:

posts_by_user = Post.objects.filter(comments__user__id=123)


https://programmer.group/data-visualization-in-python-application-downloading-data.html

https://programmer.group/django-orm-multi-table-operation-advanced.html


todoooooooooooooooooo
https://www.cnblogs.com/Michael--chen/p/10548195.html
https://programmer.group/python-big-job-crawler-visualization-data-analysis-database-visualization.html


https://programmer.group/django-orm-multi-table-operation-advanced.html
'''
class Article1(models.Model):
    ARTICLE_STATUS = (
        ('tech', 'Tech'),
        ('other', 'Other'),
    )
    category = models.CharField(max_length=255, choices=ARTICLE_STATUS)
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author1, related_name='articles', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    class Meta:
        db_table = "articless"
        verbose_name = "Articlee"
        verbose_name_plural = "Articless"

    '''
    With **kwargs
    Author.objects.filter(name='Mihail', age=20)
    SELECT "authors"."id",
       "authors"."name",
       "authors"."age"
    FROM   "authors"
    WHERE  (
        "authors"."name" = mihail AND "authors"."age" = 20
    )

    '''

    @property
    def get_books_count(self):
        return Author1.objects.filter(author=self.id).count()
