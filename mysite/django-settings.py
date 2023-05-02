import os
import django

# Set the DJANGO_SETTINGS_MODULE environment variable
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')

# Call django.setup()

django.setup()

# Now you can use Django functionality, such as models or the ORM
from myapp.models import MyModel
results = MyModel.objects.all()