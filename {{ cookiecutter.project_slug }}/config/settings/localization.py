from config import env

from config.env import BASE_DIR

LANGUAGE_CODE = 'ru'

TIME_ZONE = env.str('SERVER_TIMEZONE', 'Europe/Moscow')

USE_I18N = True

USE_TZ = True

LOCALE_PATHS = [BASE_DIR / "locales"]