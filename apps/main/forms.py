from django.forms import ModelForm, TextInput, Textarea, DateTimeInput
from .models import Article


class ArticleEditForm(ModelForm):
    class Meta:
    	model = Article
    	fields = ['title', 'body', 'created_date']


    	widgets = {
    		"title": TextInput(attrs={
    				'class': 'form-control form-title',
    				'placeholder': '| Title',
    			}),
    		"body": Textarea(attrs={
    				'placeholder': 'Your story...',
    				'rows': 10,
    			}),
    		"created_date": DateTimeInput(attrs={
    				'class': 'form-control',  				
    			})
    	}
