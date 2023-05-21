from django.contrib import admin
from django.utils.text import slugify
import uuid
import sys

from .models import Question, Choice


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]
    fieldsets = [
        (None, {"fields": ["question_text", "featured"]}),
        ("Date info", {"fields": ["pub_date"]}),
    ]
    list_display = ("question_text", "slug", "pub_date",
                    "was_published_recently", "featured", "total_votes", "id")
    list_filter = ["pub_date"]
    search_fields = ["question_text"]
    exclude = ["hashed_id", "slug"]
    readonly_fields = ('pub_date',)

    def save_related(self, request, form, formsets, change):
        obj = form.instance
        obj.total_votes = 0
        post_items_list = list(request.POST)
        wordsearch = 'votes'
        iterator = [item for item in post_items_list if wordsearch in item]
        iter_len = len(iterator)-1
        t_votes = 0
        for index in range(iter_len):
            print(f'choice_set-{index}-votes')
            t_votes += int(request.POST[f'choice_set-{index}-votes'])
        obj.total_votes = t_votes
        obj.save()
        return super().save_related(request, form, formsets, change)

    def save_model(self, request, obj, form, change):
        if not obj.slug:
            obj.slug = slugify(obj.question_text)
        return super().save_model(request, obj, form, change)


class ChoiceAdmin(admin.ModelAdmin):
    readonly_fields = ['id', 'question', 'choice_text', 'votes']
    raw_id_fields = ['question']
    list_display = ('choice_text', 'votes', 'question',  'id')

    def has_add_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions


admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice, ChoiceAdmin)
