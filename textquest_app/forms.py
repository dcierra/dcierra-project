from django.forms import ModelForm
from .models import Location, Variant, CharacterProfile


class LocationForm(ModelForm):
    class Meta:
        model = Location
        fields = [
            'location_name',
            'text',
            'image',
        ]

    def __init__(self, *args, **kwargs):
        super(LocationForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})


class VariantForm(ModelForm):
    class Meta:
        model = Variant
        fields = [
            'title',
            'next_location',
        ]

    def __init__(self, *args, **kwargs):
        super(VariantForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})


class CharacterProfileForm(ModelForm):
    class Meta:
        model = CharacterProfile
        fields = [
            'name',
            'bio',
            'image',
            'version',
        ]

    def __init__(self, *args, **kwargs):
        super(CharacterProfileForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})
