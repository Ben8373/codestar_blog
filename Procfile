release: python manage.py migrate
web: gunicorn codestar.wsgi --bind 0.0.0.0:$PORT

