from .models import Weather
from django.forms import ModelForm


class WeatherForm(ModelForm):
    class Meta:
        model = Weather
        fields = [
            'city'
        ]

    def __init__(self, *args, **kwargs):
        super(WeatherForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})
