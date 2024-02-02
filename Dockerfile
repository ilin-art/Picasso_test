FROM python:3.11

ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE file_upload_project.settings

RUN apt-get update -y
RUN apt-get upgrade -y \
    && apt-get install -y sqlite3 \
    && apt-get clean

WORKDIR /app
COPY . /app/

RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "file_upload_project.wsgi:application"]
