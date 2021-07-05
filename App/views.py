from django import forms
from App.models import Todo
from django.shortcuts import redirect, render
from .form import TodoForm, CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required(login_url='login')
def home(request):
    if request.user.is_authenticated:
        form = TodoForm()
        todo = Todo.objects.filter(user=request.user)[::-1]
        # print(todo)
    if request.method == "POST":
        if request.user.is_authenticated:
            form = TodoForm(request.POST)
            if form.is_valid():
                real_todo = form.save(commit=False)
                real_todo.user = request.user
                real_todo.save()
                print("Task is been save")
            return redirect('home')

    context = {'form': form, 'todo': todo}
    return render(request, 'home.html', context)


@login_required(login_url='login')
def delete(request, pk):
    item = Todo.objects.get(id=pk)
    if request.method == "POST":
        item.delete()
        return redirect('home')

    context = {'item': item}
    return render(request, 'confirm.html', context)


@login_required(login_url='login')
def update(request, pk):
    id = Todo.objects.get(id=pk)

    form = TodoForm(instance=id)
    if request.method == "POST":
        form = TodoForm(request.POST, instance=id)
        form.save()
        return redirect('home')
    context = {'form': form}
    return render(request, "update.html", context)


def sign_up(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    context = {'form': form}
    return render(request, "signup.html", context)


def loginpage(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            messages.warning(request, "Username or Password is incorrect")
    context = {}
    return render(request, 'login.html', context)


def logout_page(request):
    logout(request)
    return redirect('login')
