import time
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.base import View
from django.http import HttpResponse, HttpResponseRedirect
from django.utils.text import slugify
from .models import Article
from .forms import ArticleEditForm


def Create(request):
    if request.user.is_authenticated:
        error = ''
        if request.method == 'POST':
            article_form = ArticleEditForm(request.POST)
            # check whether it's valid:
            if article_form.is_valid():
                Article.objects.update_or_create(
                    title=request.POST.get("title"),
                    body=request.POST.get("body"),
                    author=request.user,
                    url=slugify(request.POST.get("title") + "-" + str(time.strftime("%m-%d")))
                )
                return HttpResponseRedirect(slugify(request.POST.get("title") + "-" + str(time.strftime("%m-%d"))))
            else:
                error = 'Form is invalid'
        article_form = ArticleEditForm()
        data = {
            'article_form': article_form,
            'error': error,
            'color': 'dark'
            }
        
        return render(request, 'main/index.html', data)
    else:
        return render(request, 'main/login.html')

# def ArticleView():
#     pass

def ArticleViewEdit(request, slug):
    instance = Article.objects.get(url=slug)
    article_form = ArticleEditForm(request.POST or None, instance=instance)
    if article_form.is_valid():
        instance.title=request.POST.get("title")
        instance.body=request.POST.get("body")
        instance.save()
        return redirect('index')
    else:
        error = 'Form is invalid'
    context = {
        'article_form': article_form,
        'error': error,
        'color': 'success',
        'form_status': True
    }
    return render(request, 'main/index.html', context)