from django import forms

from store.models import Product, Version

from django.forms import ModelForm, BooleanField

FORBIDDEN_WORDS = [
    "казино",
    "криптовалюта",
    "крипта",
    "биржа",
    "дешево",
    "бесплатно",
    "обман",
    "полиция",
    "радар",
]


# def clean(cleaned_data):
#     for word in FORBIDDEN_WORDS:
#         if word in cleaned_data.lower():
#             raise forms.ValidationError(f"Нельзя использовать слово {word}")
#     return cleaned_data


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for fild_name, field in self.fields.items():
            if isinstance(field, BooleanField):
                field.widget.attrs["class"] = "form-check-input"
            else:
                field.widget.attrs["class"] = "form-control"


class ProductForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'description', 'images', 'category', 'price', 'created_at', 'is_published')


class ProductModeratorForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Product
        fields = ('description', 'category', 'is_published',)

    def clean_name(self):
        cleaned_data = self.cleaned_data.get('name')
        for word in FORBIDDEN_WORDS:
            if word in cleaned_data.lower():
                raise forms.ValidationError(f"Нельзя использовать слово: '{word.upper()}'")
        return cleaned_data

    def clean_description(self):
        cleaned_data = self.cleaned_data.get('description')
        for word in FORBIDDEN_WORDS:
            if word in cleaned_data.lower():
                raise forms.ValidationError(f"Нельзя использовать слово: '{word.upper()}'")
        return cleaned_data


class VersionForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Version
        fields = '__all__'
