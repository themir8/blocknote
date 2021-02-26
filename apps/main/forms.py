from django.forms import ModelForm, TextInput, Textarea, DateTimeInput
from .models import Article


class ArticleEditForm(ModelForm):
    class Meta:
    	model = Article
    	fields = ['title', 'body']


    	widgets = {
    		"title": TextInput(attrs={
    				'class': 'form-control form-title',
    				'placeholder': 'Title',
    			}),
    		"body": Textarea(attrs={
                    'class': 'form-control',
    				'placeholder': 'Your story...',
    				'rows': 10,
    			})
    	}
