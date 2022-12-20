from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import ReviewForm, ProjectForm
from dcierra.utils import paginate, search_data
from .models import Project, Review


def pyqt_projects(request):
    projects, search_query = search_data(request, 'projects')

    paginator, custom_range, projects = paginate(request, projects, 3)

    context = {'projects': projects, 'custom_range': custom_range, 'paginator': paginator, 'search_query': search_query}
    return render(request, 'pyqt_app/pyqt_projects.html', context)


def pyqt_project_page(request, project_id):
    project = Project.objects.get(id=project_id)
    form = ReviewForm

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        review = form.save(commit=False)

        try:
            old_review = Review.objects.get(user=request.user.profile.id, project=project)
            old_review.review_body = review.review_body
            old_review.save()
        except:
            review.project = project
            review.user = request.user.profile
            review.save()

        project.likes_count

        messages.success(request, f'{request.user.profile}, вы успешно оставили комментарий!')
        return redirect('pyqt_project_page', project_id=project.id)

    context = {'project': project, 'form': form}
    return render(request, 'pyqt_app/pyqt_project_page.html', context)


@login_required(login_url='login')
def pyqt_project_vote(request, project_id, vote_value):
    project = Project.objects.get(id=project_id)
    user = request.user.profile

    # try:
    #     review = Review.objects.get(user=user, project=project)
    # except:
    #     review = Review.objects.create(
    #         user=user,
    #         project=project
    #     )

    review, created = Review.objects.get_or_create(
        user=user,
        project=project,
    )

    review.value = vote_value
    review.save()
    project.likes_count

    return redirect('pyqt_project_page', project_id=project_id)


@staff_member_required(login_url='login')
def pyqt_project_create(request):
    profile = request.user.profile
    form = ProjectForm

    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.owner = profile
            project.save()
            return redirect('account')

    context = {'form': form}
    return render(request, 'pyqt_app/pyqt_project_form.html', context)


@staff_member_required(login_url='login')
def pyqt_project_update(request, project_id):
    profile = request.user.profile
    project = profile.project_set.get(id=project_id)
    form = ProjectForm(instance=project)

    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            return redirect('account')

    context = {'form': form}
    return render(request, 'pyqt_app/pyqt_project_form.html', context)


@staff_member_required(login_url='login')
def pyqt_project_delete(request, project_id):
    profile = request.user.profile
    project = profile.project_set.get(id=project_id)

    if request.method == 'POST':
        project.delete()
        return redirect('account')

    context = {'object': project.title}
    return render(request, 'delete_object.html', context)
