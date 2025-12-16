import sys
import os
import django

from django.contrib.auth import get_user_model

# Add the project's parent directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'the_fasting_ox_python_django_api.settings')

django.setup()


def is_superuser_available (name):
    user = get_user_model()
    superusers = user.objects.filter(is_superuser=True)
    available = "yes"
    for superuser in superusers:
        if superuser.username == name:
            available = "no"
    return available

if __name__ == "__main__":
    # Print the result to standard output
    name = sys.argv[1]
    print(is_superuser_available(name))
    sys.exit(0) # Exit with success code
