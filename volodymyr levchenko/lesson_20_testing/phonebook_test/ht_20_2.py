import phonebook
import unittest
import json

class TestPhonebook(unittest.TestCase):
    def test_read_data(self):
        self.assertEqual(phonebook.read_data('empty_data.json'), {})

    def test_change_data(self):
        a = 1001
        file = 'some_data.json'
        phonebook.change_data(file, a)
        with open('some_data.json', 'r') as file:
            a_ = json.loads(file.read())
        self.assertEqual(a, a_)

    def test_add_new_contact(self):
        file = 'empty_data.json'
        phonebook.add_new_contact(file)
        contact_dict = {'123': {'city': 'Kyiv',
         'first_name': 'Volodymyr',
         'last_name': 'Levchenko',
         'state': 'Ukraine'}}
        with open(file, 'r') as file:
            contact_dict_ = json.loads(file.read())
        self.assertEqual(contact_dict, contact_dict_)

if __name__ == '__main__':
    unittest.main()