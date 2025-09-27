from pathlib import Path

# Базовая директория проекта
BASE_DIR = Path(__file__).resolve().parent.parent

# Секретный ключ для безопасности приложения
SECRET_KEY = 'django-insecure-=x#u*b$$9#%%9rf&&5=*&!p^fwa1pu36lrs#t%yewgusa9ttn^'

# Режим отладки
DEBUG = True

# Разрешенные хосты для работы приложения
ALLOWED_HOSTS = ['localhost', '127.0.0.1']

# Установленные приложения Django
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_filters',
    'rangefilter',  # Фильтры по диапазону дат для админки
    'main.apps.MainConfig',  # Основное приложение проекта
    'rest_framework',  # Django REST Framework для API
]

# Middleware для обработки запросов и ответов
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware', 
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Основной файл конфигурации URL-маршрутов
ROOT_URLCONF = 'dds_app.urls'

# Настройки шаблонов
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / "templates"],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# WSGI-приложение для работы с сервером
WSGI_APPLICATION = 'dds_app.wsgi.application'

# Настройки базы данных (SQLite)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Валидаторы паролей для безопасности
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Настройки интернационализации
LANGUAGE_CODE = 'ru-ru'
TIME_ZONE = 'Asia/Vladivostok'
USE_I18N = True
USE_TZ = True

# Настройки статических файлов
STATIC_URL = 'static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
STATIC_ROOT = BASE_DIR / 'staticfiles'

# Тип первичного ключа по умолчанию
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
