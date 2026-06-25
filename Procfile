release: python manage.py migrate
web: gunicorn codestar_blog.wsgi --bind 0.0.0.0:$PORT

