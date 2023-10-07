from django import forms

from .models import *

form_stats = [('', 'Any')] + STATUS_CH


class SearchForm(forms.Form):
    search = forms.CharField(widget=forms.TextInput(
        attrs={'type': 'search'}), required=False)
    languages = forms.ModelChoiceField(
        queryset=Language.objects.all(), required=False, empty_label='Any')
    company = forms.ModelChoiceField(
        queryset=Company.objects.all(), required=False, empty_label='Any')
    status = forms.ChoiceField(choices=form_stats, required=False)
