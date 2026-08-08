



## docker commands

Restore backup:
`docker compose exec -T db pg_restore -U personaltools -d personaltools --clean --no-owner < ~/personaltools-****.backup`

Django manage.py:
`docker compose exec web python manage.py makemigrations`

`docker compose exec web python manage.py migrate`