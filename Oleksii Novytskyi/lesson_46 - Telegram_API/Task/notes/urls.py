from django.urls import path

from . import views

app_name = 'notes'

urlpatterns = [
    # path('index/', views.index, name='index'),
    # path('', views.IndexView.as_view(), name='notes'),
    path('<int:note_id>/to_telegram/', views.send_notes_to_telegram, name='to_telegram'),
    path('', views.notes, name='notes'),
    path('create/', views.create_note, name='create'),
    path('<int:note_id>/delete/', views.delete_note, name='delete'),
    path('<int:note_id>/correct/', views.correct_note, name='correct'),
    path('filter/', views.filter_notes, name='filter'),
    path('find/', views.find_notes, name='find'),
    path('search/', views.search, name='search'),
    path('sign_up/', views.sign_up, name='sign_up'),

]