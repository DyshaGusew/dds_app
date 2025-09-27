````markdown
````
# ДДС (Движение Денежных Средств)

Веб-приложение на Django для управления записями о движении денежных средств (ДДС).

## Установка

1. Клонируйте репозиторий:
   ```bash
   git clone <repository_url>
   cd dds_app
   ```


2. Создайте и активируйте виртуальное окружение:

   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate  # Windows
   ```

3. Установите зависимости:

   ```bash
   pip install -r requirements.txt
   ```

4. Примените миграции:

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. Создайте суперпользователя для доступа к админке:

   ```bash
   python manage.py createsuperuser
   ```

6. Запустите сервер:
   ```bash
   python manage.py runserver
   ```

## Основные функции

- **Главная страница**: Список записей ДДС с фильтрами по дате, статусу, типу, категории и подкатегории (`/admin/main/ddsrecord/`).
- **Создание/редактирование**: Форма с динамической фильтрацией подкатегорий в админке.
- **Справочники**: Управление категориями, подкатегориями, статусами и типами через админ-панель (`/admin/main/category/`, `/admin/main/subcategory/`, `/admin/main/status/`, `/admin/main/type/`,).
- **API**: REST API для управления записями и справочниками (`/api/ddsrecords/`, `/api/statuses/`, и т.д.).

## API

- **Список записей ДДС**: `GET /api/ddsrecords/`
  - Фильтры: `?date_created=YYYY-MM-DD`, `?status=id`, `?type=id`, `?category=id`, `?sub_category=id`
- **Создание записи ДДС**: `POST /api/ddsrecords/`
  - Пример тела запроса:
    ```json
    {
      "date_created": "2025-09-27",
      "status_id": 1,
      "type_id": 1,
      "category_id": 1,
      "sub_category_id": 1,
      "amount": 100.0,
      "comment": "Тестовая запись"
    }
    ```
- **Статусы**: `GET/POST/PUT/DELETE /api/statuses/`
- **Типы**: `GET/POST/PUT/DELETE /api/types/`
- **Категории**: `GET/POST/PUT/DELETE /api/categories/`
- **Подкатегории**: `GET/POST/PUT/DELETE /api/subcategories/`

## Зависимости

- asgiref==3.9.2
- Django==5.2.6
- django-admin-rangefilter==0.13.3
- django-filter==25.1
- djangorestframework==3.16.1
- sqlparse==0.5.3
- tzdata==2025.2

## Доступ

- Админ-панель: `http://127.0.0.1:8000/admin/`
- API: `http://127.0.0.1:8000/api/`

```

```
