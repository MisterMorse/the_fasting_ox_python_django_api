#!/bin/sh

# Exit immediately if a command exits with a non-zero status.
set -e

# Wait for the PostgreSQL database service to be available.
echo "Waiting for PostgreSQL..."
while ! nc -z "${DATABASE_HOST}" "${DATABASE_PORT}"; do
  echo "Waiting at ${DATABASE_HOST}:${DATABASE_PORT}..."
  sleep 1s
done
echo "PostgreSQL started."

# Run migrations.
python manage.py migrate --noinput

# Create Django Superuser using environment variables.
if [ "$DJANGO_SUPERUSER_USERNAME" ] && [ "$DJANGO_SUPERUSER_EMAIL" ] && [ "$DJANGO_SUPERUSER_PASSWORD" ]; then
  echo "Creating Django superuser: $DJANGO_SUPERUSER_USERNAME"
  available=$(python ./utils/utils.py "$DJANGO_SUPERUSER_USERNAME")
  if [ "$available" = "yes" ]; then
    python manage.py createsuperuser --noinput \
        --username "$DJANGO_SUPERUSER_USERNAME" \
        --email "$DJANGO_SUPERUSER_EMAIL"
    echo "Django superuser created."
  else
    echo "Django superuser not created. Superuser with given username already exists."
  fi
fi

# Execute the main command passed to the container.
exec "$@"
