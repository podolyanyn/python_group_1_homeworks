from django.test import TestCase
from django.urls import reverse
from .models import Category, Note


class NoteTestCase(TestCase):
    def setUp(self):
        self.category = Category.objects.create(title='Test Category')

    def test_create_category(self):
        response = self.client.post(reverse('create_category'), {'title': 'New Category'})
        self.assertEqual(response.status_code, 302)  # Проверяем, что после создания категории происходит перенаправление
        self.assertTrue(Category.objects.filter(title='New Category').exists())  # Проверяем, что категория создана

    def test_delete_category(self):
        response = self.client.post(reverse('delete_category', args=[self.category.id]))
        self.assertEqual(response.status_code, 302)  # Проверяем, что после удаления категории происходит перенаправление
        self.assertFalse(Category.objects.filter(id=self.category.id).exists())  # Проверяем, что категория удалена

    def test_create_two_categories(self):
        response = self.client.post(reverse('create_category'), {'title': 'Category 1'})
        self.assertEqual(response.status_code, 302)
        response = self.client.post(reverse('create_category'), {'title': 'Category 2'})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Category.objects.count(), 3)  # Проверяем, что созданы две новые категории

    def test_create_note(self):
        response = self.client.post(reverse('create_note'), {
            'title': 'Test Note',
            'content': 'Note content',
            'category': self.category.id
        })

        self.assertTrue(Note.objects.filter(title='Test Note').exists())
        self.assertEqual(response.status_code, 302)

    def test_edit_note(self):
        note = Note.objects.create(title='Note 1', content='Note content', category=self.category)
        response = self.client.post(reverse('edit_note', args=[note.id]), {
            'title': 'Updated Note',
            'content': 'Updated content',
            'category': self.category.id
        })

        note.refresh_from_db()
        self.assertEqual(note.title, 'Updated Note')
        self.assertEqual(note.content, 'Updated content')
        self.assertEqual(response.status_code, 302)

    def test_delete_note(self):
        note = Note.objects.create(title='Note 1', content='Note content', category=self.category)
        response = self.client.post(reverse('delete_note', args=[note.id]))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Note.objects.filter(id=note.id).exists())

    def test_search_notes(self):
        note1 = Note.objects.create(title='Note 1', content='Note content 1', category=self.category)
        note2 = Note.objects.create(title='Note 2', content='Note content 2', category=self.category)
        response = self.client.get(reverse('search_notes'), {'query': 'Note 1'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, note1.title)
        self.assertNotContains(response, note2.title)
