from django.core.exceptions import ValidationError


def validate_file_size(value):
    filesize = value.size

    if filesize > 1048576:
        raise ValidationError("Максимальный размер загружаемого файла не может превышать 1МБ")
    else:
        return value


def validate_file_extension(value):
    file_content_type = value.file.content_type

    if file_content_type not in ['application/octet-stream']:
        raise ValidationError("Расширение не поддерживается")
    else:
        return value
