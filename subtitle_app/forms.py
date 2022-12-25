from django.forms import ModelForm
from .models import Subtitle
from django import forms


class SubtitleForm(ModelForm):
    class Meta:
        model = Subtitle
        fields = [
            'original_file',
            'translation_language',
        ]

    def __init__(self, *args, **kwargs):
        super(SubtitleForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})
