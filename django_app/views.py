from django.shortcuts import render


def django_projects(request):
    context = {}
    return render(request, 'django_app/django_projects.html', context)
