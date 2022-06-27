up:
	docker-compose up -d
migrate:
	docker compose exec web python manage.py migrate 
create:
	@make migrate
	docker compose exec web python manage.py createsuperuser
addmodels:
	docker compose exec web python manage.py makemigrations 
	@make migrate