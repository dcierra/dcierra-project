import re

from django.core.exceptions import ValidationError


def validate_file_size(value):
    filesize = value.size

    if filesize > 104857600:
        raise ValidationError("Максимальный размер загружаемого файла не может превышать 1000МБ")
    else:
        return value


def validate_file_extension(value):
    file_content_type = value.file.content_type

    if file_content_type not in ['application/vnd.rar', 'application/x-rar-compressed',
                                 'application/zip', 'application/x-7z-compressed',
                                 'application/octet-stream']:
        raise ValidationError("Расширение не поддерживается")
    else:
        return value

def validate_filename(value):
    pattern = re.compile(r'^[a-zA-Z0-9_]+\.[a-zA-Z]{3,4}$')
    if not pattern.match(value.name):
        raise ValidationError('Имя файла должно быть на английском языке')
