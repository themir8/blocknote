from django.shortcuts import render, redirect
from django.views.generic.base import View
from django.http import HttpResponse, HttpResponseRedirect
from .models import Article
from .forms import ArticleForm


def Create(request):
    error = ''
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            form.save()
            return redirect('index')
        # if a GET (or any other method) we'll create a blank form
        else:
            error = 'Form is invalid'
    form = ArticleForm()
    data = {
        'form': form,
        'error': error
        }
    
    return render(request, 'main/index.html', data)

def ArticleViewEdit(request, slug):

    data = {
        'el': Article.objects.get(url=slug)
    }

    return render(request, 'main/index.html', data)