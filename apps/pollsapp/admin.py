from django.contrib import admin
from django.utils.text import slugify
import sys

from .models import Question, Choice


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["question_text"]}),
        ("Date info", {"fields": ["pub_date"]}),
    ]
    list_display = ("id", "hashed_id", "slug",
                    "question_text", "pub_date", "was_published_recently")
    list_filter = ["pub_date"]
    search_fields = ["question_text"]
    exclude = ["hashed_id", "slug"]
    readonly_fields = ('pub_date',)
    inlines = [ChoiceInline]

    def save_model(self, request, obj, form, change):
        if not obj.hashed_id:
            obj.hashed_id = str(hash(obj.id) % ((sys.maxsize + 1) * 2))
        if not obj.slug:
            obj.slug = slugify(obj.question_text)
        return super().save_model(request, obj, form, change)


admin.site.register(Question, QuestionAdmin)
