build:
	docker-compose build

up:
	docker-compose up -d

down:
	docker-compose down

migrations:
	docker-compose exec app python manage.py migrate

create_superuser:
	docker-compose exec app python manage.py createsuperuser