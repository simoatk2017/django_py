from django.db import models

# Create your models here.
'''
In the example above, ***** Comment will be the target of any on_delete handler when you delete Post, 
but not the other way around.****** If you delete a Comment instance, nothing will happen to  Post.
class Post(models.Model):
	title = models.CharField(max_length=255)

class Comment(models.Model):
	content = models.TextField()  #👇🏻
	post = models.ForeignKey(Post, on_delete=[?])



models.CASCADE

Let’s take our Post and Comment example and set on_delete to models.CASCADE

class Comment(models.Model):
	...  #                                          👇🏻
	post = models.ForeignKey(Post, on_delete=models.CASCADE)

When we call post.delete(), it will cascade down to the foreign key relationship(s). Meaning that both Post and Comment get deleted.
'''

'''
https://www.geeksforgeeks.org/how-to-create-a-basic-api-using-django-rest-framework/

rest api
https://tests4geeks.com/blog/django-rest-framework-tutorial/
'''


class GeeksModel(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title


'''
Each Model here is related to a table in the database. 
As we don’t have these tables in the database yet, 
let’s create a rule to make them (in Django these rules are called migrations):
'''
'''
drf-jwt-example
https://github.com/sibtc/drf-jwt-example
'''


class University(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = "University"
        verbose_name_plural = "Universities"

    def __str__(self):
        return self.name


class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    university = models.ForeignKey(University, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Student"
        verbose_name_plural = "Students"

    def __unicode__(self):
        return '%s %s' % (self.first_name, self.last_name)
