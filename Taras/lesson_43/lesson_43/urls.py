"""
URL configuration for lesson_43 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app_1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('note_list/', views.note_list, name='note_list'),
    path('create_note/', views.create_note, name='create_note'),
    path('note_details/<int:note_id>/', views.note_details, name='note_details'),
    path('delete_note/<int:note_id>/', views.delete_note, name='delete_note'),
]
