from django.shortcuts import render, redirect
from .models import Task
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model, login

CustomUser = get_user_model()

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']

        user = CustomUser.objects.create(username=username, email=email, first_name=first_name, last_name=last_name)
        user.set_password(password)
        user.save()
        login(request, user)
       # return redirect('task_list')
    return render(request, 'register.html') 

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user) 
            return redirect('task_list')
        else:
            return render(request, 'login.html', {'error': 'Invalid username or password'})

    return render(request, 'login.html')

@login_required
def create_task(request):
    if request.method=='POST':
        title = request.POST['title']
        description = request.POST['description']
        due_date = request.POST['due_date']
        status = request.POST['status']

        task = Task.objects.create(title=title, description=description, due_date=due_date, status=status)
    return render(request, 'Create.html')

@login_required
def update(request, id):
    task = Task.objects.get(id=id)
    
    if request.method=='POST':
        task.title = request.POST['title']
        task.description = request.POST['description']
        task.due_date = request.POST['due_date']
        task.status = request.POST['status']
        task.save()
        return redirect('task_list')
    
    context = {
        'task': task
    }
    return render(request, 'Create.html', context)

@login_required
def delete(request, id):
    task = Task.objects.get(id=id)
    task.delete()
    return redirect('task_list')

@login_required
def task_list(request):
    task = Task.objects.all()
    context = {
        'task' : task
    }
    return render(request, 'task_list.html', context)

@login_required
def logout_user(request):
    logout(request)
    return redirect('login')

@login_required
def user_detail(request):
    user=request.user
    context = {
        'user': user
    }
    return render(request, 'user.html', context)