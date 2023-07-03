from django import forms
from .models import Note, Category
from django.forms import TimeInput


class NoteForm(forms.ModelForm):
    reminder_date = forms.DateField(
        input_formats=['%d.%m.%Y', '%Y-%m-%d'],  # Add the desired input formats here
        widget=forms.DateInput(attrs={'class': 'datepicker'})
    )
    reminder_time = forms.TimeField(
        widget=TimeInput(format='%H:%M', attrs={'class': 'timepicker'})
    )

    class Meta:
        model = Note
        fields = ('title', 'content', 'category', 'reminder_date', 'reminder_time')
        widgets = {
            'category': forms.Select(attrs={'class': 'selectpicker'}),
        }

    def __init__(self, *args, **kwargs):
        super(NoteForm, self).__init__(*args, **kwargs)
        self.fields['category'].empty_label = 'Выберите категорию'
        self.fields['category'].queryset = Category.objects.all()


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('title',)
