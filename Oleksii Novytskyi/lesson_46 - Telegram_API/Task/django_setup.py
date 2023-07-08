import os
import django

def setup_django():
    # Визначаємо шлях до файлу settings.py
    settings_module = os.path.splitext(os.path.basename(__file__))[0] + '.settings'

    # Встановлюємо змінну оточення DJANGO_SETTINGS_MODULE
    # os.environ.setdefault('DJANGO_SETTINGS_MODULE', settings_module)
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'notes_app.settings')
    # Запускаємо налаштування Django
    django.setup()