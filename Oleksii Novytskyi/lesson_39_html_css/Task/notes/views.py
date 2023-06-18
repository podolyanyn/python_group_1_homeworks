from django.http import HttpResponse
# from django.contrib.auth.models import User
from django.shortcuts import render

def index(request):
    return HttpResponse("Hello from Notes app.")


def notes(request):
    # перелік рористувачів
    # notes_list = User.objects.all()
    notes_list = ['note_1', 'note_2', 'note_3', 'note_4', 'note_5']
    context = {'notes_list': notes_list}
    return render(request, 'notes/index.html', context)