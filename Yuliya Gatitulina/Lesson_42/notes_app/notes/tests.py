from django.test import TestCase
from django.urls import reverse
from .models import Notes,Category
from .forms import NotesForm
from django.utils import timezone
from datetime import datetime

class NotesTestCase(TestCase):
    def setUp(self):
        self.category = Category.objects.create(title='Test Category')
        self.note = Notes.objects.create(
            title='Test Note',
            text='This is a test note',
            reminder = timezone.make_aware(datetime(2023, 6, 28, 10, 0, 0), timezone.get_current_timezone()),
            category=self.category
        )

    def test_new_note_view(self):
        form_data = {
            'title': 'New Note',
            'text': 'This is a new note',
            'reminder': '2023-07-01 12:00:00',
            'category': self.category.id
        }
        response = self.client.post(reverse('notes:new_note'), data=form_data)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Notes.objects.count(), 2)

    def test_change_note_view(self):
        form_data = {
            'title': 'Updated Note',
            'text': 'This is an updated note',
            'reminder': '2023-06-29 15:00:00',
            'category': self.category.id
        }
        url = reverse('notes:change_note', args=[self.note.id])
        response = self.client.post(url, data=form_data)
        self.assertEqual(response.status_code, 302)
        self.note.refresh_from_db()
        self.assertEqual(self.note.title, 'Updated Note')

    def test_delete_note_view(self):
        url = reverse('notes:delete_note', args=[self.note.id])
        response = self.client.post(url)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Notes.objects.count(), 0)