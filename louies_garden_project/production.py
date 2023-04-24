from .settings import *

DEBUG = False

ALLOWED_HOSTS = ['https://louies-garden.onrender.com/','louies-garden.onrender.com', 'louiesgarden.com', 'www.louiesgarden.com']


# Use the environment variable for the secret key
SECRET_KEY = os.environ['SECRET_KEY']


# Configure static files
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'

# Add any other production-specific settings here
