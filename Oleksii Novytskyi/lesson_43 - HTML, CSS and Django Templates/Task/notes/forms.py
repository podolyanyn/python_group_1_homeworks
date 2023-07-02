from django import forms
from .models import Notes, Categories


class NotesForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = ['categories', 'title', 'text', 'reminder']


# class SearchForm(forms.ModelForm):
#     class Meta:
#         model = Notes
#         fields = ['category', 'title', 'content']
#         widgets = {
#             'category': forms.Select(attrs={'class': 'form-select'}),
#             'title': forms.Select(attrs={'class': 'form-select'}),
#             'reminder': forms.Select(attrs={'class': 'form-select'}),
#         }

