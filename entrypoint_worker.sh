#!/bin/sh
echo "Inicializando WORKER"

cd app/
celery -A liftit_demo worker -l info
