'''
The development settings file is meant to be used in development. 
'''

from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '^vb=_m2$*bv1*@ssrw@d37dqfryj_q-l7kr7ve(khu4^x5j)4k'

ALLOWED_HOSTS = ['localhost', '127.0.0.1']

# Custom setting, used in core.utils.full_reverse()
DEFAULT_DOMAIN = 'http://localhost:8000'

# Database https://docs.djangoproject.com/en/3.0/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

"""
Because we can't include a default email account (w/ password), the only way to
get dev emails to work "out of the box" is to use the file (or console) backend.
This basically "sends" emails to log files in the django_project/.emails/
directory. The dot is there to differentiate the emails folder from a django app
which happens to live in the same directory.

More info:
https://docs.djangoproject.com/en/stable/topics/email/#email-backends

If you want to add your own email account, see local_example.py
"""
EMAIL_BACKEND = 'django.core.mail.backends.filebased.EmailBackend'
EMAIL_FILE_PATH = os.path.join(BASE_DIR, '.emails')
