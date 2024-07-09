from config import env

LANGUAGE_CODE = 'ru'

TIME_ZONE = env.str('SERVER_TIMEZONE', 'Europe/Moscow')

USE_I18N = True

USE_TZ = True
