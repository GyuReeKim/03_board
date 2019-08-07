from django.shortcuts import render
from .models import Todo

# Create your views here.
def new(request):
    return render(request, 'new.html')

def create(request):
    title = request.GET.get('title')
    content = request.GET.get('content')
    due_date = request.GET.get('due-date')
    # print(title, content, due_date)

    todo = Todo()
    todo.title = title
    todo.content = content
    todo.due_date = due_date
    # 데이터를 넣고 저장을 하지 않았기에 save()를 해줘야 데이터베이스에 반영된다.
    todo.save()

    # todo = Todo(title=title, content=content, due_date=due_date)
    # todo.save()

    return render(request, 'create.html')

def index(request):
    todos = Todo.objects.all()
    context = {
        'todos': todos,
    }
    return render(request, 'index.html', context)

def detail(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    context = {
        'todo': todo,
    }
    return render(request, 'detail.html', context)