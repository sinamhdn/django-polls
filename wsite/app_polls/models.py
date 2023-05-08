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

    @admin.display(
        boolean=True,
        ordering="pub_date",
        description="Published recently?",
    )
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    def get_absolute_url(self):
        return reverse("app_polls:detail", args=[str(self.id), str("%s-%s" % (self.hashed_id, self.slug))])


class Choice(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4(), editable=False)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
