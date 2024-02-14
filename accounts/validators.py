from django.core.exceptions import ValidationError
import os


def allow_images(value):
    ext = os.path.splitext(value.name)[1] # for file format
    print(ext)
    valid_extension = ['.png','.jpg','.jpeg']
    if not ext.lower() in valid_extension:
        raise ValidationError('Unsupported file extension. Allowed extension:' + str(valid_extension))