from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render, redirect
from dcierra.utils import paginate, search_data
from .forms import ProjectForm
from .models import Project


def django_projects(request):
    projects, search_query = search_data(request, 'django_projects')

    paginator, custom_range, projects = paginate(request, projects, 3)

    context = {'projects': projects, 'custom_range': custom_range, 'paginator': paginator, 'search_query': search_query}
    return render(request, 'django_app/django_projects.html', context)


@staff_member_required(login_url='login')
def django_project_create(request):
    form = ProjectForm

    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('account')

    context = {'form': form}
    return render(request, 'django_app/django_project_form.html', context)


@staff_member_required(login_url='login')
def django_project_update(request, project_id):
    project = Project.objects.get(id=project_id)
    form = ProjectForm(instance=project)

    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            return redirect('account')

    context = {'form': form}
    return render(request, 'django_app/django_project_form.html', context)


@staff_member_required(login_url='login')
def django_project_delete(request, project_id):
    project = Project.objects.get(id=project_id)

    if request.method == 'POST':
        project.delete()
        return redirect('account')

    context = {'object': project.title}
    return render(request, 'delete_object.html', context)
