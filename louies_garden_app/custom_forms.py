from django import forms
from .constants import VEGETABLE_CHOICES

class AddForm(forms.Form):
    width = forms.CharField(max_length=500, label="Plot width")
    height = forms.CharField(max_length=500, label="Plot length")
    zipcode = forms.CharField(max_length=500, label="Zip code")
    vegetables = forms.MultipleChoiceField(
        choices=VEGETABLE_CHOICES,
        widget=forms.CheckboxSelectMultiple,
        label="Vegetables",
        required=False,
    )

class AddAskForm(forms.Form):
    question = forms.CharField(max_length=500, label="Quesion")

  