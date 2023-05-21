from django.db import models
from django.db.models import F
from django.urls import reverse
from django.contrib import admin
from django.utils import timezone
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _
import datetime


class Question(models.Model):
    question_text = models.CharField(max_length=200, null=False)
    pub_date = models.DateTimeField("date published", auto_now_add=True)
    total_votes = models.PositiveIntegerField(default=0)
    featured = models.BooleanField(default=False)
    slug = models.SlugField()

    def __str__(self):
        return self.question_text

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.question_text)
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
        return reverse("pollsapp:detail", args=[str(self.id), str(self.slug)])


class Choice(models.Model):
    choice_text = models.CharField(max_length=200)
    votes = models.PositiveIntegerField(default=0)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return self.choice_text
