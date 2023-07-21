from django.test import TestCase
from django.urls import reverse
from .models import Notes, Categories
from datetime import datetime
from django.utils.timezone import make_aware


class CorrectNoteViewTest(TestCase):

    def test_correct_note_view_response_status(self):
        note = Notes.objects.create(
            categories=Categories.objects.create(title="Category"),
            title="Title",
            text="Text",
            reminder=make_aware(datetime(2023, 6, 27, 10, 0))
        )

        url = reverse('notes:correct', args=[note.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_correct_note_view_template(self):
        note = Notes.objects.create(
            categories=Categories.objects.create(title="Category"),
            title="Title",
            text="Text",
            reminder=make_aware(datetime(2023, 6, 27, 10, 0))
        )
        url = reverse('notes:correct', args=[note.id])
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'notes/correct_note.html')

    def test_correct_note_view_instance_form(self):
        note = Notes.objects.create(
            categories=Categories.objects.create(title="Category"),
            title="Title",
            text="Text",
            reminder=make_aware(datetime(2023, 6, 27, 10, 0))
        )
        url = reverse('notes:correct', args=[note.id])
        response = self.client.get(url)
        form = response.context['form']
        self.assertEqual(form.instance, note)

