#!/bin/sh

# Exit immediately if a command exits with a non-zero status.
set -e

# Wait for the PostgreSQL database service to be available.
echo "Waiting for PostgreSQL..."
while ! nc -z db 5432; do
  sleep 0.1
done
echo "PostgreSQL started."

# Run migrations.
python manage.py migrate --noinput

# Create Django Superuser using environment variables.
if [ "$DJANGO_SUPERUSER_USERNAME" ] && [ "$DJANGO_SUPERUSER_EMAIL" ] && [ "$DJANGO_SUPERUSER_PASSWORD" ]; then
  echo "Creating Django superuser: $DJANGO_SUPERUSER_USERNAME"
  python manage.py createsuperuser --noinput \
      --username "$DJANGO_SUPERUSER_USERNAME" \
      --email "$DJANGO_SUPERUSER_EMAIL"
  echo "Django superuser created."
fi

# Execute the main command passed to the container.
exec "$@"
