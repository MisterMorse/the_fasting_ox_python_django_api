# Stage 1: Base build stage.
FROM python:3.13-slim AS builder

# Create the app directory.
RUN mkdir /app

# Set environment variables to optimize Python.
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PYTHONPATH="/app"
ENV DJANGO_SETTINGS_MODULE="the_fasting_ox_python_django_api.settings"

# Set the working directory.
WORKDIR /app

# Upgrade pip and install dependencies.
RUN pip install --upgrade pip

# Copy the requirements file first (better caching).
COPY requirements.txt /app/

# Install Python dependencies.
RUN pip install --no-cache-dir -r requirements.txt

# Stage 2: Production stage.
FROM python:3.13-slim

# Switch to root user, install package for waiting behavior,
# copy the entrypoint script into the container, and make it executable.
USER root
RUN apt-get update && apt-get install -y netcat-openbsd && rm -rf /var/lib/apt/lists/*

# Create a non-root user and group.
RUN groupadd -r appgroup && useradd -r -g appgroup appuser && \
   mkdir /app && \
   chown -R appuser /app

# Copy the Python dependencies from the builder stage.
COPY --from=builder /usr/local/lib/python3.13/site-packages/ /usr/local/lib/python3.13/site-packages/
COPY --from=builder /usr/local/bin/ /usr/local/bin/

# Set the working directory.
WORKDIR /app

# Copy the application code.
COPY . /app/

# Give the appuser ownership of the application directory.
RUN chown -R appuser:appgroup /app

# Switch to the non-root user.
USER appuser

# Set environment variables to optimize Python.
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

ENV DJANGO_SECRET_KEY=${DJANGO_SECRET_KEY}
ENV DEBUG=${DEBUG}
ENV DJANGO_LOGLEVEL=${DJANGO_LOGLEVEL}
ENV DJANGO_ALLOWED_HOSTS=${DJANGO_ALLOWED_HOSTS}
ENV DATABASE_ENGINE=${DATABASE_ENGINE}
ENV DATABASE_NAME=${DATABASE_NAME}
ENV DATABASE_USER=${DATABASE_USER}
ENV DATABASE_PASSWORD=${DATABASE_PASSWORD}
ENV DATABASE_HOST=${DATABASE_HOST}
ENV DATABASE_PORT=${DATABASE_PORT}
ENV DJANGO_SUPERUSER_USERNAME=${DJANGO_SUPERUSER_USERNAME}
ENV DJANGO_SUPERUSER_EMAIL=${DJANGO_SUPERUSER_EMAIL}
ENV DJANGO_SUPERUSER_PASSWORD=${DJANGO_SUPERUSER_PASSWORD}

# Expose the application port.
EXPOSE 8000

# Set the entrypoint.
COPY ./entrypoint.sh /app/entrypoint.sh
ENTRYPOINT [ "/app/entrypoint.sh" ]

# Set the default command (will be passed as arguments to the entrypoint script via "$@").
CMD [ "gunicorn", "--bind", ":8000", "the_fasting_ox_python_django_api.wsgi:application" ]
# Or for development:
# CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]
