from django.contrib import admin
from django.utils.text import slugify
import sys

from .models import Question, Choice


class QuestionAdmin(admin.ModelAdmin):
    list_display = ("hashed_id", "slug",
                    "question_text", "pub_date",)
    exclude = ["hashed_id", "pub_date", "slug",]

    def save_model(self, request, obj, form, change):
        if not obj.hashed_id:
            obj.hashed_id = str(hash(obj.id) % ((sys.maxsize + 1) * 2))
        if not obj.slug:
            obj.slug = slugify(obj.question_text)
        return super().save_model(request, obj, form, change)


class ChoiceAdmin(admin.ModelAdmin):
    list_display = ("choice_text", "votes",)


admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice, ChoiceAdmin)
