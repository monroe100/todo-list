from django.shortcuts import render
from django.http import HttpResponse
from .models import Todo

# Create your views here.
def index(request):
    todos = Todo.objects.all()[:10]

    context = {
        'todos':todos
    }

    return render(request, 'index.html', context)