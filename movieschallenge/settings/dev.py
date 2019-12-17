from .base import *

# MongoDB conf
DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'NAME': 'moviesdb',
        'HOST': 'localhost',
        'PORT': 27017,
    }
}
