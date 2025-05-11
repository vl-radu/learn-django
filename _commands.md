## Django
```
### Create superuser (if not done already)
```
python manage.py createsuperuser
```
### Restart Django Container
```
docker-compose restart django
```
### Extract SQL from database
```
python manage.py inspectdb > models.py
```