from django.shortcuts import render, redirect
from .models import TodoItem
from django.contrib.auth.decorators import login_required



# Create your views here.

def home(request):
    todoitems = TodoItem.objects.all()
    todolist =  TodoItem.objects.filter(check=False)
    print(todolist)
    todolen = len(todolist)
    context = {"todoitems":todoitems, "todolen":todolen}
    return render(request, "todolist.html", context)


@login_required
def createTodo(request):
    todoitem = request.POST["todoitem"]
    TodoItem.objects.create(content=todoitem)
    return redirect('home')

@login_required
def toggleTodo(request, pk):
    todoItem = TodoItem.objects.get(pk=pk)
    if todoItem.check:
        todoItem.check = False
        todoItem.save()
    else:
        todoItem.check = True
        todoItem.save()
    return redirect('home')

@login_required
def deleteTodo(request, pk):
    todoitem = TodoItem.objects.get(pk=pk)
    todoitem.delete()
    return redirect('home')