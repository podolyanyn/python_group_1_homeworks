from django import forms
from .models import Note, Category


class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ('title', 'content', 'category')

    def __init__(self, *args, **kwargs):
        super(NoteForm, self).__init__(*args, **kwargs)
        self.fields['category'].empty_label = 'Выберите категорию'
        self.fields['category'].queryset = Category.objects.all()


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('title',)
