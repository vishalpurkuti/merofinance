from django.db.models import fields
from django import forms
from .models import IncomeCategory


class AddIncomeCategoryForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control'}))

    class Meta:
        model = IncomeCategory
        fields = ['title', ]
