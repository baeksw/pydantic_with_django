
run:
	python manage.py runserver

migrate:
	python manage.py migrate

admin:
	# admin#1123
	python manage.py createsuperuser --email admin@example.com --username admin
