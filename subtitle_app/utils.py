import pysubs2
import requests
import threading
from .models import Subtitle


def translate_subtitle(sub, translation_language):
    translate_url = f"https://translate.googleapis.com/translate_a/single?client=gtx&sl=auto&" \
                    f"tl={translation_language}&dt=t&q={sub.text}"

    response = requests.get(translate_url)
    translation = response.json()[0][0][0]

    sub.text = translation


def translate_subtitles(subtitle_id):
    subtitle = Subtitle.objects.get(id=subtitle_id)
    input_file = subtitle.original_file

    translation_language = subtitle.translation_language
    threads = []

    subs = pysubs2.load(f'static/images/{input_file.name}')

    for sub in subs:
        t = threading.Thread(target=translate_subtitle, args=(sub, translation_language))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    name_output_file = f'{translation_language}.{input_file.name.split("/")[1]}'
    output_file = f'static/images/output_files_subtitle/{name_output_file}'
    subs.save(output_file)
    return f'images/output_files_subtitle/{name_output_file}'
