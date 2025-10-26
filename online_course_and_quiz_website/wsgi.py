import sys
import os

path = '/home/dheerajk553/online-course-and-quiz-website-new'
if path not in sys.path:
    sys.path.append(path)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "online_course_and_quiz_website.settings")

from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()
