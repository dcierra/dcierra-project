import re

from django.core.exceptions import ValidationError


def validate_file_size(value):
    filesize = value.size

    if filesize > 5242880:
        raise ValidationError("Максимальный размер загружаемого файла не может превышать 5МБ")
    else:
        return value


def validate_file_extension(value):
    file_content_type = value.file.content_type

    if file_content_type not in ['application/pdf', 'application/msword',
                                 'application/vnd.openxmlformats-officedocument.wordprocessingml.document']:
        raise ValidationError("Расширение не поддерживается")
    else:
        return value

def validate_filename(value):
    pattern = re.compile(r'^[a-zA-Z0-9_]+\.[a-zA-Z]{3,4}$')
    if not pattern.match(value.name):
        raise ValidationError('Имя файла должно быть на английском языке')
