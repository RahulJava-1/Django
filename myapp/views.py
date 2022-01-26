from django.shortcuts import render,redirect
from .models import Todo

# Create your views here.
def index(request):
    item=Todo.objects.all()
    con = {'item':item}
    return render(request,'index.html',con)

def form(request):
    return render(request,'form.html')

#receive all the value from form
def add(request):
    t=request.POST['title']
    d=request.POST['description']
    save=Todo(title=t,description=d)
    save.save()
    return redirect('index')

def delete(request,id):
        d = Todo.objects.get(id=id)
        d.delete()
        return redirect('index')
