#!/bin/bash

APP=/app
export PYTHONIOENCODING="UTF-8"
export DB_NAME=catalog
export DB_USER=catalog
export DB_HOST=localhost
export DB_PORT=5432
export UWSGI_PORT=443
export SOCKET_FILE=uwsgi.sock
export STATS_PORT=1717

function waitpidkilled {
    pid=$1
    while ps -p $pid > /dev/null
    do
      sleep 1;
      echo "Wait for it..."
    done
}

if [ "$#" = 0 ]; then
    echo "Usage: "
    echo --manage [options] Run manage.py
    echo --prod  Run the application with production settings
    echo --stopuwsgi Stop uwsgi workers
fi

if [ "$1" = '--manage' ]; then
    $APP/manage.py "${@:2}"
    exit $?
fi

if [ "$1" = '--prod' ]; then
    export DJANGO_STATIC_ROOT=/uwsgi/static
    $APP/manage.py collectstatic --noinput
    $APP/manage.py migrate --noinput
    uwsgi --ini $APP/uwsgi.ini --socket "/uwsgi/$SOCKET_FILE" --http ":$UWSGI_PORT" --stats ":$STATS_PORT"
    touch /uwsgi/uwsgi.log
    tail -f /uwsgi/uwsgi.log
    exit $?
fi

if [ "$1" = '--stopuwsgi' ]; then
    echo q > /tmp/uwsgififo
    echo "Told workers to stop"
    pid=$(cat /tmp/uwsgi.pid)
    waitpidkilled $pid
    echo "uwsgi gracefully stopped"
    exit $?
fi

"$@"
