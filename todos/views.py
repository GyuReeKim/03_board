from django.shortcuts import render, redirect
from .models import Todo

# Create your views here.
def new(request):
    return render(request, 'new.html')

def create(request):
    # GET 요청을 받아서 new.html의 name="title"의 정보를 title에 저장해준다.
    title = request.GET.get('title')
    content = request.GET.get('content')
    due_date = request.GET.get('due-date')
    # print(title, content, due_date)

    # 1번
    # models.py에 저장되어있는 class Todo의 정보를 인스턴스 todo에 저장한다.
    todo = Todo()
    todo.title = title
    todo.content = content
    todo.due_date = due_date
    # 데이터를 넣고 저장을 하지 않았기에 save()를 해줘야 데이터베이스에 반영된다.
    todo.save()

    # 2번
    # todo = Todo(title=title, content=content, due_date=due_date)
    # todo.save()

    # return render(request, 'create.html')
    # render를 쓰는것도 가능하지만 코드의 흐름이 달라진다.
    return redirect('/todos/')

def index(request):
    # models.py에 저장되어있는 class Todo의 인스턴스 todo에서 모든 정보를 가져온다.
    # 빠른 날짜 순서대로 정렬
    todos = Todo.objects.order_by('due_date').all()
    # 빠른 날짜 반대 순서로 정렬
    # todos = Todo.objects.order_by('due_date').all()
    context = {
        'todos': todos,
    }
    return render(request, 'index.html', context)

def detail(request, todo_id):
    # models.py에 저장되어있는 class Todo의 인스턴스 todo에서 id 정보를 가져온다.
    todo = Todo.objects.get(id=todo_id)
    context = {
        'todo': todo,
    }
    return render(request, 'detail.html', context)

def delete(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    todo.delete()
    # return render(request, 'delete.html')
    return redirect('/todos/')

def edit(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    context = {
        'todo': todo,
    }
    return render(request, 'edit.html', context)
    
def update(request, todo_id):
    title = request.GET.get('title')
    content = request.GET.get('content')
    due_date = request.GET.get('due-date')

    todo = Todo.objects.get(id=todo_id)
    todo.title = title
    todo.content = content
    todo.due_date = due_date
    # models.Model에 .save()등 많은 함수들이 저장되어 있다.
    todo.save()

    # return render(request, 'update.html')
    return redirect(f'/todos/{todo_id}/')
    # 아래처럼 todo.id도 가능
    # return redirect(f'/todos/{todo.id}/detail')