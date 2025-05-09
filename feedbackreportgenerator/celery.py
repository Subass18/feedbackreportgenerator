import os
from celery import Celery

# Set default Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'feedbackreportgenerator.settings')

# Initialize Celery application
app = Celery('feedbackreportgenerator')

# Load configuration from Django settings, using 'CELERY_' namespace
app.config_from_object('django.conf:settings', namespace='CELERY')

# Auto-discover tasks from installed apps
app.autodiscover_tasks()
