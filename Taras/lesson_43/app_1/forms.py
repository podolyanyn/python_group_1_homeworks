from django import forms


class NoteForm(forms.Form):
    title = forms.CharField(label='Назва')
    text = forms.CharField(label='Текст', widget=forms.Textarea)
    reminder = forms.DateTimeField(label='Нагадування', widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))
    category = forms.CharField(label='Категорія')