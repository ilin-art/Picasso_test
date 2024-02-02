from celery import shared_task
from .models import File


@shared_task
def process_uploaded_file(file_id, mime_type):
    try:
        file = File.objects.get(id=file_id)
        file.processed = True

        if 'image' in mime_type:
            print("Изображение обработано")
        elif 'text' in mime_type:
            print("Текст обработан")
        else:
            print("Файл обработан")

        file.save()
    except Exception as e:
        print(f'Error processing file: {e}')
        raise
