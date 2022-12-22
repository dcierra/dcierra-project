from .models import Todo
from django.forms import ModelForm


class TodoForm(ModelForm):
    class Meta:
        model = Todo
        fields = [
            'title',
            'description',
            'important',
        ]

    def __init__(self, *args, **kwargs):
        super(TodoForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})
