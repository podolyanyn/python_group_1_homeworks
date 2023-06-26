from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
#from django.contrib.auth.models import User

def index(request):
    return HttpResponse("Hello from Notes app.")

def notes(request):
    notes_list = ['note 1', 'note 2', 'note 3', 'note 4', 'note 5', 'note 6', 'note 7']
    context = {"notes_list": notes_list}
    return render(request, "notes/index.html", context)