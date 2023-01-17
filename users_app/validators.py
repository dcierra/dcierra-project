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
