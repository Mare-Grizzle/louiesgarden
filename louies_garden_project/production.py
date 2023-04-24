from .settings import *

DEBUG = False

ALLOWED_HOSTS = ['https://louies-garden.onrender.com/','louies-garden.onrender.com', 'louiesgarden.com', 'www.louiesgarden.com']


# Use the environment variable for the secret key
SECRET_KEY = os.environ['SECRET_KEY']

BASE_DIR = Path(__file__).resolve().parent.parent

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'

# production.py
MIDDLEWARE = [
    # ...
    'whitenoise.middleware.WhiteNoiseMiddleware',
    # ...
]

# Add this line to enable GZip compression for static files
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'



# Add any other production-specific settings here
