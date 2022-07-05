from django import forms
from .models import Blog, Comment, Category
from django.core.exceptions import ValidationError


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('title', 'content',)

        def clean(self):
            print('validationssssssssssssssssssss')
            clear_data = super(BlogForm, self).clean()
            title = self.clean().get('title')
            if len(title) < 10:
                raise forms.ValidationError('nnnnnnnnnnnnnnnnnnnn')
            return title


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = "__all__"



class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'text',)
        '''
        def clean_text(self):
            print('validationssssssssssssssssssss')
            clear_data = super(CommentForm, self).clean()
            text = self.cleaned_data('text')
            print('sex')
            if 'sex' in text:
                print(111111111111)
                raise ValidationError('nnnnnnnnnnnnnnnnnnnn')
            return text
        '''

        def clean_text(self):
            print('nameeeeeeeeeeeeeeeeeee')
            text = self.cleaned_data['text']
            if len(text) < 20:
                raise forms.ValidationError('The max length of firstName is 20 characters')
            return text
