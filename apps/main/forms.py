from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Article


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(widget=forms.TextInput(
            attrs={
            'class': 'form-control form-title'}))
    firstname = forms.CharField(max_length=100, 
        widget=forms.TextInput(
            attrs={
            'class': 'form-control form-title'}))
    lastname = forms.CharField(max_length=100, widget=forms.TextInput(
            attrs={
            'class': 'form-control form-title'}))

    class Meta:
        model = User
        fields = ['username', 'firstname', 'lastname', 'email', 'password1', 'password2']


class ArticleEditForm(forms.ModelForm):
    class Meta:
    	model = Article
    	fields = ['title', 'body']


    	widgets = {
    		"title": forms.TextInput(attrs={
    				'class': 'form-control form-title',
    				'placeholder': 'Title',
    			}),
    		"body": forms.Textarea(attrs={
                    'class': 'form-control',
    				'placeholder': 'Your story...',
    				'rows': 10,
    			})
    	}
