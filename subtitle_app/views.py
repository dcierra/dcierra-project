from django.shortcuts import render
from .forms import SubtitleForm
from .utils import translate_subtitles


def subtitle_home_page(request):
    form = SubtitleForm()

    if request.method == 'POST':
        form = SubtitleForm(request.POST, request.FILES)

        if form.is_valid():
            subtitle = form.save(commit=False)

            subtitle_id = subtitle.id
            subtitle.save()

            name_output_file = translate_subtitles(subtitle_id)

            context = {'form': form, 'name_output_file': name_output_file}
            return render(request, 'subtitle_app/subtitle_home_page.html', context)

    context = {'form': form}
    return render(request, 'subtitle_app/subtitle_home_page.html', context)
