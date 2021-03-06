from django.db import models as db
from django.contrib.auth.models import User
from django.utils import timezone
from ckeditor.fields import RichTextField
from simple_history.models import HistoricalRecords
from simple_history import register


register(User)


class Article(db.Model):
    title = db.CharField("Название", max_length=50)
    body = RichTextField()
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
        verbose_name = "Пост"
        verbose_name_plural = "Посты"