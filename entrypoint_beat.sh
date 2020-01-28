#!/bin/sh
echo "Inicializando BEAT"
sleep 2
cd app/
celery -A liftit_demo beat -l info
