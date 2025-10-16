"""
WSGI config for online_course_and_quiz_website project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""
import sys
import os
path = '/home/dheerajk553/online-course-and-quiz-website'
if path not in sys.path:
    sys.path.append(path)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'online_course_and_quiz_website.settings')

from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()
