from django.db import models as db
from django.contrib.auth.models import User
from django.utils import timezone
from ckeditor.fields import RichTextField
from tinymce import models as tinymce_models
from simple_history.models import HistoricalRecords

import time
from django.utils.text import slugify


class Article(db.Model):
    title = db.CharField("Название", max_length=50)
    body = tinymce_models.HTMLField()
    url = db.SlugField("Ссылка", max_length=60, unique=True)
    draft = db.BooleanField("Черновик", default=False)
    author = db.ForeignKey(
        User, verbose_name = "Имя ползователя", on_delete=db.SET_NULL, null=True
    )
    created_date = db.DateTimeField("Дата")
    history = HistoricalRecords()


    def __str__(self):
        return self.title


    def save(self, *args, **kwargs):
        if not self.created_date:
            self.created_date = timezone.now()
        super(Article, self).save(*args, **kwargs)
        


    def get_absolute_url(self):
        return f"{self.url}"


    class Meta:
        verbose_name = "Article"
        verbose_name_plural = "Articles"


class GroupArticles(db.Model):
    """ GroupArticles model demo version :) """

    name = db.CharField("Group name", max_length=80)
    description = db.TextField("Group description")
    author = db.ForeignKey(
        User, verbose_name = "Group author", on_delete=db.CASCADE
    )
    articles = db.ManyToManyField(
        Article, verbose_name='Articles'
    )
    private = db.BooleanField("Private goup?", default=False)
    slug = db.SlugField("Url to group", max_length=60, unique=True)
    created_date = db.DateTimeField("Group created date")
    history = HistoricalRecords()


    def __str__(self):
        return self.name


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name + "-" + str(time.strftime("%m-%d")))
        if not self.created_date:
            self.created_date = timezone.now()
        super(GroupArticles, self).save(*args, **kwargs)


    class Meta:
        verbose_name = "Group Article"
        verbose_name_plural = "Group Articles"


# Register a User model for simple_history
from simple_history import register
register(User)
#