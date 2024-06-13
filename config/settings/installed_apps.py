THIRD_PARTY_APPS = [
    'ninja',
    'corsheaders',
]

INTERNAL_APPS = [
    'common.apps.CommonConfig',
]

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    *THIRD_PARTY_APPS,
    *INTERNAL_APPS,
]
