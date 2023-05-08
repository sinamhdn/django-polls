from django.contrib import admin
from django.utils.text import slugify
import sys

from .models import Question, Choice


class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fields = ["pub_date", "question_text"]
    fieldsets = [
        (None, {"fields": ["question_text"]}),
        ("Date information", {"fields": ["pub_date"]}),
    ]
    list_display = ("question_text", "pub_date",)
    exclude = ["hashed_id", "pub_date", "slug",]
    inlines = [ChoiceInline]

    def save_model(self, request, obj, form, change):
        if not obj.hashed_id:
            obj.hashed_id = str(hash(obj.id) % ((sys.maxsize + 1) * 2))
        if not obj.slug:
            obj.slug = slugify(obj.question_text)
        return super().save_model(request, obj, form, change)
    # prepopulated_fields = {"slug": ("question_text",)}


admin.site.register(Question, QuestionAdmin)


class ChoiceAdmin(admin.ModelAdmin):
    list_display = ("choice_text", "votes",)


admin.site.register(Choice, ChoiceAdmin)
