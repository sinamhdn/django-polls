from django.contrib import admin
from django.utils.text import slugify
import sys

from .models import Question, Choice


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    list_display = ("id", "hashed_id", "slug",
                    "question_text", "pub_date", "was_published_recently")
    list_filter = ["pub_date"]
    search_fields = ["question_text"]
    exclude = ["hashed_id", "pub_date", "slug",]
    inlines = [ChoiceInline]

    def save_model(self, request, obj, form, change):
        if not obj.hashed_id:
            obj.hashed_id = str(hash(obj.id) % ((sys.maxsize + 1) * 2))
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

    def save_model(self, request, obj, form, change):
        global total_votes
        total_votes += request.votes
        print('TOTAL VOTES2: ', total_votes)
        return super().save_model(request, obj, form, change)


admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice, ChoiceAdmin)
