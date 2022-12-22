from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .forms import TodoForm
from dcierra.utils import paginate, search_data


@login_required(login_url='login')
def home_page(request):
    todos, search_query = search_data(request, 'todos')
    paginator_todos, custom_range_todos, todos = paginate(request, todos, 5)

    completed_todos, search_query = search_data(request, 'completed_todos')
    paginator_complete_todo, custom_range_completed_todos, completed_todos = paginate(request, completed_todos, 5)

    context = {'todos': todos, 'custom_range_todos': custom_range_todos, 'paginator_todos': paginator_todos,
               'completed_todos': completed_todos, 'custom_range_completed_todos': custom_range_completed_todos,
               'paginator_complete_todo': paginator_complete_todo}

    return render(request, 'todo_app/todo_home_page.html', context)


@login_required(login_url='login')
def todo_create(request):
    form = TodoForm()
    profile = request.user.profile

    if request.method == 'POST':
        form = TodoForm(request.POST)
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
    form = TodoForm(instance=todo)

    if request.method == 'POST':
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('todo_home_page')

    context = {'form': form}
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
