from users_app.models import Profile, Message
from django_app.models import Project as DjangoProject
from pyqt_app.models import Project
from django.db.models import Q
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def paginate(request, data, results):
    page = request.GET.get('page')
    paginator = Paginator(data, results)

    try:
        data = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        data = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        data = paginator.page(page)

    leftIndex = (int(page) - 1)
    if leftIndex < 1:
        leftIndex = 1

    rightIndex = (int(page) + 1)
    if rightIndex > paginator.num_pages:
        rightIndex = paginator.num_pages

    custom_range = range(leftIndex, rightIndex + 1)

    return paginator, custom_range, data


def search_data(request, data_name, category_id=None):
    search_query = ''

    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')

    try:
        user = request.user.profile
    except:
        user = None

    if user:
        data = {
            'profiles': profiles_set_filter(search_query),
            'inbox': inbox_set_filter(search_query, request.user.profile.messages.all()),
            'projects': projects_set_filter(search_query),
            'django_projects': django_projects_set_filter(search_query),
            'todos': todos_filter(request.user, category_id),
            'completed_todos': completed_todos_filter(request.user, category_id),
            'weather': request.user.profile.weather_set.filter(main_city=False),
        }
    else:
        data = {
            'profiles': profiles_set_filter(search_query),
            'projects': projects_set_filter(search_query),
            'django_projects': django_projects_set_filter(search_query),
        }

    return data.get(data_name), search_query


# filter
def profiles_set_filter(search_query):
    set_filter = Profile.objects.distinct().filter(
        Q(username__icontains=search_query) |
        Q(first_name__icontains=search_query) |
        Q(second_name__icontains=search_query) |
        Q(about_myself__icontains=search_query)
    )
    return set_filter


def inbox_set_filter(search_query, messages):
    set_filter = messages.distinct().filter(
        Q(first_name__icontains=search_query) |
        Q(email__icontains=search_query) |
        Q(subject__icontains=search_query)
    )
    return set_filter


def projects_set_filter(search_query):
    set_filter = Project.objects.distinct().filter(
        Q(title__icontains=search_query) |
        Q(description__icontains=search_query) |
        Q(owner__username__icontains=search_query)
    )

    return set_filter


def django_projects_set_filter(search_query):
    set_filter = DjangoProject.objects.distinct().filter(
        Q(title__icontains=search_query) |
        Q(description__icontains=search_query)
    )

    return set_filter


def todos_filter(user, category_id):
    if category_id:
        set_filter = user.profile.todo_set.filter(date_completed__isnull=True, category=category_id)
    else:
        set_filter = user.profile.todo_set.filter(date_completed__isnull=True)

    return set_filter


def completed_todos_filter(user, category_id):
    if category_id:
        set_filter = user.profile.todo_set.filter(date_completed__isnull=False, category=category_id)
    else:
        set_filter = user.profile.todo_set.filter(date_completed__isnull=False)

    return set_filter
