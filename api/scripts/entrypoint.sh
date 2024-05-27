#!/bin/sh

# "$DB_HOST" "$DB_PORT" should be changed to corresponding db env variables
# note that in order for this entrypoint to work netcat must be installed

echo "Waiting for postgres ..."

while ! nc -z "$DB_HOST" "$DB_PORT"; do
  sleep 0.1
  done

  echo "PostgreSQL started"


python manage.py collectstatic --no-input --clear
python manage.py migrate
python manage.py load_data
python manage.py runserver 0.0.0.0:8000

exec "$@"
