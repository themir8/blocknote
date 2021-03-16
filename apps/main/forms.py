from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import password_validation
from django import forms
from tinymce.widgets import TinyMCE
from .models import Article


class UserRegistrationForm(UserCreationForm):
    """This form for registration users"""
    
    firstname = forms.CharField(
        max_length=100, 
        widget=forms.TextInput(attrs={'class': 'form-control'}))

    lastname = forms.CharField(
        max_length=100, 
        widget=forms.TextInput(attrs={'class': 'form-control'}))

    username = forms.CharField(
        max_length=100, 
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        help_text="Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.")

    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control'}))

    password1 = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        help_text=password_validation.password_validators_help_text_html(),
    )
    password2 = forms.CharField(
        label="Password confirmation",
        widget=forms.PasswordInput(attrs={'class': 'form-control', 
                                            'autocomplete': 'new-password'}),
        strip=False,
        help_text="Enter the same password as before, for verification.",
    )

    class Meta:
        model = User
        fields = ['firstname', 'lastname', 'username', 'email', 'password1', 'password2']


class ArticleEditForm(forms.ModelForm):
    class Meta:
    	model = Article
    	fields = ['title', 'body']


    	widgets = {
    		"title": forms.TextInput(attrs={
    				'class': 'form-control form-title',
    				'placeholder': 'Title',
    			}),
    		"body": TinyMCE(attrs={'cols': 80, 'rows': 30})
            }
