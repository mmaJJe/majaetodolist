from django.shortcuts import render, redirect
from .models import TodoItem

# Create your views here.

def home(request):
    todoitems = TodoItem.objects.all()
    todolist =  TodoItem.objects.filter(check=False)
    print(todolist)
    todolen = len(todolist)
    context = {"todoitems":todoitems, "todolen":todolen}
    return render(request, "todolist.html", context)

def createTodo(request):
    todoitem = request.POST["todoitem"]
    TodoItem.objects.create(content=todoitem)
    return redirect('home')

def toggleTodo(request, pk):
    todoItem = TodoItem.objects.get(pk=pk)
    if todoItem.check:
        todoItem.check = False
        todoItem.save()
    else:
        todoItem.check = True
        todoItem.save()
    return redirect('home')

def deleteTodo(request, pk):
    todoitem = TodoItem.objects.get(pk=pk)
    todoitem.delete()
    return redirect('home')