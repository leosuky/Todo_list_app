from django.shortcuts import render
from django.utils import timezone
from .models import Todo
from django.http import HttpResponseRedirect


# Create your views here.
def home(request):
    todo_items = Todo.objects.all().order_by('-added_date')
    return render(request, 'Todo_listapp/add_todo.html', {"todo_items": todo_items})


def add_todo(request):
    z_date = timezone.now()
    content = request.POST['content']
    created_obj = Todo.objects.create(added_date=z_date, text=content)
    # print(z_date)
    # print(content)
    # print(created_obj)
    # print(created_obj.id)
    return HttpResponseRedirect("/")

def delete_todo(request, todo_id):
    Todo.objects.get(id=todo_id).delete()
    return HttpResponseRedirect("/")