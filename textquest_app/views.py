from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render, redirect
from .forms import LocationForm, VariantForm, CharacterProfileForm
from .models import Location, Variant, CharacterProfile
from django.conf import settings


def text_quest_home_page(request, location_id=settings.START_LOCATION_ID):
    try:
        user = request.user.profile
    except:
        user = None

    print(user.quest_location_id)
    if user and user.quest_location_id:
        if location_id != settings.START_LOCATION_ID:
            user.quest_location_id = location_id
            user.save()
            location = Location.objects.get(id=user.quest_location_id)
        else:
            location = Location.objects.get(id=user.quest_location_id)
    else:
        if user:
            user.quest_location_id = location_id
            user.save()
        location = Location.objects.get(id=location_id)

    context = {'location': location}
    return render(request, 'textquest_app/text_quest_home_page.html', context)


def character_profile(request, character_id):
    character = CharacterProfile.objects.get(id=character_id)
    context = {'character': character}
    return render(request, 'textquest_app/character-profile.html', context)


@staff_member_required(login_url='login')
def create_character(request):
    form = CharacterProfileForm()

    if request.method == 'POST':
        form = CharacterProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('text_quest_home_page')

    context = {'form': form}
    return render(request, 'textquest_app/character_profile_form.html', context)


@staff_member_required(login_url='login')
def edit_character(request, character_id):
    character = CharacterProfile.objects.get(id=character_id)
    form = CharacterProfileForm(instance=character)

    if request.method == 'POST':
        form = CharacterProfileForm(request.POST, request.FILES, instance=character)
        if form.is_valid():
            form.save()
            return redirect('text_quest_home_page')

    context = {'form': form}
    return render(request, 'textquest_app/character_profile_form.html', context)


@staff_member_required(login_url='login')
def delete_character(request, character_id):
    character = Location.objects.get(id=character_id)

    if request.method == 'POST':
        character.delete()

    return redirect('text_quest_home_page')


@staff_member_required(login_url='login')
def add_location(request):
    form = LocationForm()

    if request.method == 'POST':
        form = LocationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('text_quest_home_page')

    context = {'form': form}
    return render(request, 'textquest_app/location_form.html', context)


@staff_member_required(login_url='login')
def edit_location(request, location_id):
    location = Location.objects.get(id=location_id)
    form = LocationForm(instance=location)

    if request.method == 'POST':
        form = LocationForm(request.POST, request.FILES, instance=location)
        if form.is_valid():
            form.save()
            return redirect('text_quest_home_page')

    context = {'form': form, 'location_id': location.id, 'location': location}
    return render(request, 'textquest_app/location_form.html', context)


@staff_member_required(login_url='login')
def delete_location(request, location_id):
    location = Location.objects.get(id=location_id)

    if request.method == 'POST':
        location.delete()

    return redirect('text_quest_home_page')


@staff_member_required(login_url='login')
def add_variant(request, location_id):
    form = VariantForm()
    location = Location.objects.get(id=location_id)

    if request.method == 'POST':
        form = VariantForm(request.POST)
        if form.is_valid():
            variant = form.save(commit=False)
            variant.location = location
            variant.save()
            return redirect('edit_location', location_id=location_id)

    context = {'form': form}
    return render(request, 'textquest_app/variant_form.html', context)


@staff_member_required(login_url='login')
def edit_variant(request, variant_id, location_id):
    variant = Variant.objects.get(id=variant_id)
    form = VariantForm(instance=variant)

    if request.method == 'POST':
        form = VariantForm(request.POST, request.FILES, instance=variant)
        if form.is_valid():
            form.save()
            return redirect('edit_location', location_id=location_id)

    context = {'form': form}
    return render(request, 'textquest_app/variant_form.html', context)


@staff_member_required(login_url='login')
def delete_variant(request, variant_id, location_id):
    variant = Variant.objects.get(id=variant_id)

    if request.method == 'POST':
        variant.delete()

    return redirect('edit_location', location_id=location_id)
