from django import forms


class DocumentForm(forms.Form):
    docfile = forms.FileField(label="Select a file")


class DexForm(forms.Form):
    def __init__(self, dex_attributes={}, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for key, value in dex_attributes.items():
            value.insert(0, "*")
            choices = list(zip(value, value))
            self.fields[key] = forms.ChoiceField(
                choices=choices, widget=forms.Select(attrs={"class": "form-control"})
            )


class DexFormWithDescription(forms.Form):
    def __init__(self, dex_attributes={}, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for key, value in dex_attributes.items():
            choices = list(zip(value['choices'], value['choices']))
            self.fields[key] = forms.ChoiceField(
                help_text=value['description'], choices=choices, widget=forms.Select(attrs={"class": "form-control"})
            )
