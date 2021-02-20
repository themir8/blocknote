from django.forms import ModelForm, TextInput, Textarea, DateTimeInput
from django.contrib.auth.models import User
from .models import Article

user = User()

class ArticleForm(ModelForm):
    class Meta:
    	model = Article
    	fields = ['title', 'author', 'text', 'created_date']


    	widgets = {
    		"title": TextInput(attrs={
    				'class': 'form-control',
    				'placeholder': 'Title',
    			}),
    		"text": Textarea(attrs={
    				'class': 'form-control br-n',
    				'placeholder': 'Your story...',
    				'rows': 10
    			}),
    		"created_date": DateTimeInput(attrs={
    				'class': 'form-control',  
    				'placeholder': 'Date',  				
    			})
    	}
