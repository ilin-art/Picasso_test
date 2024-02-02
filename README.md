# File Upload Service

This is a sample project for a file upload service built using Django, Celery, and Redis. It allows users to upload files, which are then processed asynchronously by a Celery worker.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Docker: [Install Docker](https://docs.docker.com/get-docker/)
- Docker Compose: [Install Docker Compose](https://docs.docker.com/compose/install/)

## Getting Started

To get this project up and running, follow these steps:

1. Clone this repository:

   ```shell
   git clone https://github.com/ilin-art/Picasso_test.git
   cd upload_files

2. Build and start the services using Docker Compose:
    ```shell
    docker-compose up -d

3. Apply the database migrations:
    ```shell
    docker-compose exec web python manage.py migrate

4. Access the web application at
    ```shell
    GET http://51.250.20.80:8000/api/v1/files/ # Get all objects
    POST http://51.250.20.80:8000/api/v1/upload/ # Upload file (You can attach any file)

## Running Tests
To run the tests, use the following command:
docker-compose exec web python manage.py test

### Как изменится архитектура, если мы ожидаем большую нагрузку
1. Использовать механизм кэширования, для уменьшения нагрузки на базу данных и ускорения ответов на запросы.
Можно кэшировать часто запрашиваемые данные, которые редко изменяются.
Горизонтальное масштабирование:
2. Разместить приложение на нескольких серверах, чтобы балансировать нагрузку и повысить отказоустойчивость.
3. Асинхронная обработка.
Разбить операции на более мелкие задачи и обрабатывать их параллельно. Увеличить количество worker'ов.
