from django import forms
from django.forms import inlineformset_factory
from django.utils.translation import gettext as _

from pollsapp.utils.forms import is_empty_form, is_form_persisted
from .models import Question, Choice


class QuestionForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        # globally override the Django >=1.6 default of ':'
        kwargs.setdefault('label_suffix', '')
        super(QuestionForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'rounded question-input-form-control'

    class Meta:
        model = Question
        fields = [
            'question_text',
        ]
        labels = {
            "question_text": _(""),
        }
        localized_fields = ['__all__']


class ChoiceForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        # globally override the Django >=1.6 default of ':'
        kwargs.setdefault('label_suffix', '')
        super(ChoiceForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'rounded choice-input-form-control'

    class Meta:
        model = Choice
        fields = [
            'choice_text',
        ]
        labels = {
            "choice_text": _(""),
        }
        localized_fields = ['__all__']


ChoiceFormSet = inlineformset_factory(Question, Choice, form=ChoiceForm, extra=2, max_num=50,
                                      validate_max=True, absolute_max=1500, can_delete=False, can_delete_extra=False)
