from .models import Todo, Category
from django.forms import ModelForm


class TodoForm(ModelForm):
    class Meta:
        model = Todo
        fields = [
            'title',
            'description',
            'category',
            'important',
        ]

    def __init__(self, user, *args, **kwargs):
        super(TodoForm, self).__init__(*args, **kwargs)
        self.fields['category'].queryset = Category.objects.filter(owner=user.id)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})


class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = [
            'title',
        ]

    def __init__(self, *args, **kwargs):
        super(CategoryForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})
