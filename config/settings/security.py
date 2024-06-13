from config import env

SECRET_KEY = env.str('SECRET_KEY')

CORS_ALLOWED_ORIGINS = env.list('CORS_ALLOWED_ORIGINS', [])

CSRF_TRUSTED_ORIGINS = env.list('CSRF_TRUSTED_ORIGINS', [])

ALLOWED_HOSTS = env.list('ALLOWED_HOSTS', [])
