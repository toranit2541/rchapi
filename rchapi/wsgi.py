# """
# WSGI config for rchapi project.

# It exposes the WSGI callable as a module-level variable named ``application``.

# For more information on this file, see
# https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
# """

# import os
# import sys

# # Add your project directory to the sys.path
# sys.path.append('/home/toranit/rchapi-main')

# # Activate the virtual environment
# activate_this = '/home/toranit/rchapi-main/venv/bin/activate_this.py'
# exec(open(activate_this).read(), dict(__file__=activate_this))

# # Set the Django settings module
# os.environ['DJANGO_SETTINGS_MODULE'] = 'rchapi-main.settings'

# # Import Django WSGI application
# from django.core.wsgi import get_wsgi_application # type: ignore
# application = get_wsgi_application()


import os
import sys

# Define the base directory of the Django project
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../rchapi-main"))

# Add the project directory to the Python path
sys.path.append(BASE_DIR)

# Set the Django settings module correctly (adjust as needed)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "rchapi.settings")

# # Activate the virtual environment properly
# VENV_PATH = os.path.join(BASE_DIR, "venv")
# if os.path.exists(os.path.join(VENV_PATH, "bin", "activate")):  # Linux/macOS
#     activate_script = os.path.join(VENV_PATH, "bin", "activate")
# elif os.path.exists(os.path.join(VENV_PATH, "Scripts", "activate.bat")):  # Windows
#     activate_script = os.path.join(VENV_PATH, "Scripts", "activate.bat")
# else:
#     raise RuntimeError("Virtual environment not found!")

# Import and set up Django WSGI application
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
