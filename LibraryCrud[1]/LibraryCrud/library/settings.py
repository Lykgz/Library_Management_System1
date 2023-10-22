import os

INSTALLED_APPS = [
    # ...
    'library',
]

STATIC_URL = '/static/'
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Database settings (using SQLite as an example)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Static files (for CSS, JavaScript, and images)
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / "static"]

# Template directory
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        # ...
    },
]

# URL configuration
LOGIN_REDIRECT_URL = 'book_list'
LOGOUT_REDIRECT_URL = 'book_list'
