from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import CustomUserCreationForm, ProfileForm, MessageForm
from .models import Profile, Message
from dcierra.utils import paginate, search_data
from django_app.models import Project as DjangoProject


def home_page(request):
    try:
        profile = Profile.objects.get(username='dcierra')
    except:
        profile = request.user.profile
    context = {'profile': profile}
    return render(request, 'users_app/home_page.html', context)


# Login/Register/Logout
def register_page(request):
    form = CustomUserCreationForm()
    page = 'Регистрация'

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            if not Profile.objects.filter(username=user.username.lower()).exists():
                user.username = user.username.lower()
                user.save()

                login(request, user)
                return redirect('account_edit')

    context = {'page': page, 'form': form}
    return render(request, 'users_app/login_register.html', context)


def login_page(request):
    page = 'Авторизация'
    error = ''

    if request.user.is_authenticated:
        return redirect('home_page')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except:
            error = 'Пользователь не найден'

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home_page')
        else:
            error = 'Имя пользователя И/ИЛИ пароль введены неправильно'

    context = {'page': page, 'error': error}
    return render(request, 'users_app/login_register.html', context)


def logout_user(request):
    logout(request)
    return redirect('login')


# Account/Profile Page
def profile_user(request, profile_id):
    profile = Profile.objects.get(id=profile_id)

    context = {'profile': profile}
    return render(request, 'users_app/profile_user.html', context)


def profiles(request):
    profiles, search_query = search_data(request, 'profiles')
    paginator, custom_range, profiles = paginate(request, profiles, 3)
    context = {'profiles': profiles, 'search_query': search_query, 'paginator': paginator, 'custom_range': custom_range}
    return render(request, 'users_app/profiles.html', context)


@login_required(login_url='login')
def account_page(request):
    profile = request.user.profile
    projects = profile.project_set.all()
    django_projects = DjangoProject.objects.all()
    context = {'profile': profile, 'projects': projects, 'django_projects': django_projects}
    return render(request, 'users_app/account.html', context)


@login_required(login_url='login')
def account_edit(request):
    profile = request.user.profile
    form = ProfileForm(instance=profile)

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()

            return redirect('account')

    context = {'form': form, 'profile': profile}
    return render(request, 'users_app/account_edit.html', context)


# Messages/Inbox
@login_required(login_url='login')
def inbox(request):
    all_messages, search_query = search_data(request, 'inbox')
    paginator, custom_range, all_messages = paginate(request, all_messages, 5)

    unread_messages = request.user.profile.messages.all().filter(is_read=False).count()
    context = {'all_messages': all_messages, 'unread_messages': unread_messages, 'custom_range': custom_range,
               'paginator': paginator}
    return render(request, 'users_app/inbox.html', context)


@login_required(login_url='login')
def message_page(request, message_id):
    msg = get_object_or_404(Message, id=message_id, recipient=request.user.profile)

    if not msg.is_read:
        msg.is_read = True
        msg.save()

    context = {'message': msg}
    return render(request, 'users_app/message_page.html', context)


def send_message(request, profile_id):
    recipient = Profile.objects.get(id=profile_id)
    form = MessageForm()

    try:
        sender = request.user.profile
    except:
        sender = None

    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            msg = form.save(commit=False)
            msg.sender = sender
            msg.recipient = recipient

            if sender:
                msg.first_name = sender.first_name
                msg.email = sender.email

            msg.save()
            return redirect('profile_user', recipient.id)

    context = {'recipient': recipient, 'form': form}
    return render(request, 'users_app/send_message.html', context)


@login_required(login_url='login')
def message_delete(request, message_id):
    msg = get_object_or_404(Message, id=message_id, recipient=request.user.profile)

    if request.method == 'POST':
        msg.delete()

    return redirect('inbox')


@login_required(login_url='login')
def all_messages_delete(request):
    profile = request.user.profile
    all_messages = profile.messages.all()

    if request.method == 'POST':
        all_messages.delete()

    return redirect('inbox')
