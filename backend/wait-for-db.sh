#!/bin/sh

echo "Waiting for postgres..."

while ! nc -z postgres-service 5432; do
  sleep 1
done

echo "PostgreSQL started"

exec "$@"