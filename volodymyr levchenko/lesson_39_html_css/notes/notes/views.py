from django.http import HttpResponse
from django.shortcuts import render

def hello_view(request):
    return HttpResponse("Hello from Notes app.")


def notes_view(request):
    notes = [
        {'name':'note_1', 'note':'this is note_1'},
        {'name':'note_2', 'note':'this is note_2'},
        {'name':'note_3', 'note':'this is note_3'},
    ]
    return render(request, 'notes/index.html', {'notes':notes})