#!/bin/sh
echo "Inicializando APP"
sleep 3
python3 /app/manage.py migrate
python3 /app/manage.py runserver 0.0.0.0:5000
