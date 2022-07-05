from django.db import models

'''
Model Book has ForeignKey relations with Author model.
The Book models have a property called get_status_verbose_name this will return the verbose name of the book’s status.
'''

'''
https://www.hacksoft.io/blog/django-filter-chaining

'''
# Create your models here.
class Book(models.Model):
    BOOK_STATUS = (
        ('PUBLISHED', 'Published'),
        ('ON_HOLD', 'On Hold'),
    )
    id = models.AutoField(primary_key=True)
    book_name = models.CharField(max_length=255)
    author = models.ForeignKey('Author', on_delete=models.CASCADE, related_name='author')
    status = models.CharField(max_length=255, choices=BOOK_STATUS)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "books"
        verbose_name = "Book"
        verbose_name_plural = "Books"

    def __str__(self):
        return self.book_name

    '''
    Suppose if Book status is PUBLISHED then it will display Published for human readability.
    '''

    @property
    def get_status_verbose_name(self):
        for row in range(0, 2):
            print(self.BOOK_STATUS[row])
            if self.BOOK_STATUS[row][0] == self.status:
                status_verbose = self.BOOK_STATUS[row][1]
                break
        return status_verbose


class Author(models.Model):
    id = models.AutoField(primary_key=True)
    author_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "authors"
        verbose_name = "Author"
        verbose_name_plural = "Authors"

    def __str__(self):
        return self.author_name

    '''
       The Author Models do not have anything special but it has get_books_count property which returns the count of Books written by the Author.
    '''

    @property
    def get_books_count(self):
        return Book.objects.filter(author=self.id).count()
