from django import forms

from .models import Category, Tag


class ProductFilterForm(forms.Form):
    """
    Form for searching and filtering products.
    """

    search = forms.CharField(
        required=False,
        max_length=200,
        widget=forms.TextInput(attrs={
            'placeholder': 'Search products...',
        }),
        help_text='Search products by description keywords.',
    )
    category = forms.ModelChoiceField(
        required=False,
        queryset=Category.objects.all(),
        empty_label='All Categories',
        help_text='Filter products by category.',
    )
    tags = forms.ModelMultipleChoiceField(
        required=False,
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        help_text='Filter products by one or more tags.',
    )