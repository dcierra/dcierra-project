from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .forms import TodoForm, CategoryForm
from .models import Category, Todo
import uuid
from dcierra.utils import paginate, search_data


@login_required(login_url='login')
def home_page(request, category_id=None):
    try:
        category_id = uuid.UUID(request.GET.get('category_id'))
    except:
        category_id = None

    all_category = Category.objects.filter(owner=request.user.profile.id)

    todos, search_query = search_data(request, 'todos', category_id)
    paginator_todos, custom_range_todos, todos = paginate(request, todos, 5)

    completed_todos, search_query = search_data(request, 'completed_todos', category_id)
    paginator_complete_todo, custom_range_completed_todos, completed_todos = paginate(request, completed_todos, 5)


    context = {'todos': todos, 'custom_range_todos': custom_range_todos, 'paginator_todos': paginator_todos,
               'completed_todos': completed_todos, 'custom_range_completed_todos': custom_range_completed_todos,
               'paginator_complete_todo': paginator_complete_todo,
               'all_category': all_category, 'category_id': category_id}

    return render(request, 'todo_app/todo_home_page.html', context)


@login_required(login_url='login')
def todo_create(request):
    profile = request.user.profile
    form = TodoForm(profile)

    if request.method == 'POST':
        form = TodoForm(profile, request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.owner = profile
            todo.save()
            return redirect('todo_home_page')

    context = {'form': form}
    return render(request, 'todo_app/todo_form.html', context)


@login_required(login_url='login')
def todo_update(request, todo_id):
    profile = request.user.profile
    todo = get_object_or_404(profile.todo_set, id=todo_id)
    form = TodoForm(profile, instance=todo)

    if request.method == 'POST':
        form = TodoForm(profile, request.POST, instance=todo)
        print(request.POST['category'])
        if form.is_valid():
            form.save()
            return redirect('todo_home_page')

    context = {'form': form, 'todo_id': todo.id}
    return render(request, 'todo_app/todo_form.html', context)


@login_required(login_url='login')
def todo_delete(request, todo_id):
    profile = request.user.profile
    todo = get_object_or_404(profile.todo_set, id=todo_id)

    if request.method == 'POST':
        todo.delete()

    return redirect('todo_home_page')


@login_required(login_url='login')
def todo_complete(request, todo_id):
    profile = request.user.profile
    todo = get_object_or_404(profile.todo_set, id=todo_id)

    if request.method == 'POST':
        todo.date_completed = timezone.now()
        todo.save()

        return redirect('todo_home_page')

    return redirect('todo_home_page')


@login_required(login_url='login')
def todo_uncompleted(request, todo_id):
    profile = request.user.profile
    todo = get_object_or_404(profile.todo_set, id=todo_id)

    if request.method == 'POST':
        todo.date_completed = None
        todo.save()

        return redirect('todo_home_page')

    return redirect('todo_home_page')


@login_required(login_url='login')
def add_category(request):
    form = CategoryForm()
    profile = request.user.profile

    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            category = form.save(commit=False)
            category.owner = profile
            category.save()
            return redirect('todo_home_page')

    context = {'form': form}
    return render(request, 'todo_app/category_form.html', context)


@login_required(login_url='login')
def delete_category(request):
    category = Category.objects.filter(owner=request.user.profile.id)

    if request.method == 'POST':
        category.delete()

    return redirect('todo_home_page')
