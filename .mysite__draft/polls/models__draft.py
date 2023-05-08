from django.db import models
from django.urls import reverse
from django.contrib import admin
from django.utils import timezone
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _
import sys
import uuid
import datetime


class Question(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4(), editable=False)
    hashed_id = models.CharField(max_length=200)
    question_text = models.CharField(max_length=200, null=False)
    pub_date = models.DateTimeField("date published", auto_now_add=True)
    slug = models.SlugField()

    def __str__(self):
        return self.question_text

    def save(self, *args, **kwargs):
        if not self.hashed_id:
            self.hashed_id = str(hash(self.id) % ((sys.maxsize + 1) * 2))
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    # USE WITH EMPTY VALUES ONLY FOR DISPLAY PURPOSES
    @admin.display
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    def get_absolute_url(self):
        return reverse("detail", args=[str(self.hashed_id), str(self.slug)])
        # return reverse("question_detail", args=[str(self.id)])


class Choice(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4(), editable=False)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
