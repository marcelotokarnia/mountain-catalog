# Trekkpedia

## How to hack locally (TL;DR)

Disclaimer:

This setup instructions are focused on Linux users, if you are using MacOs or Windows, you might need to adapt.

PYTHON

* `wget http://download.osgeo.org/gdal/2.2.4/gdal-2.2.4.tar.gz -O /tmp/gdal-2.2.4.tar.gz && tar -x -f /tmp/gdal-2.2.4.tar.gz -C /tmp`

* `cd /tmp/gdal-2.2.4 && ./configure --prefix=/usr --with-python --with-geos --with-curl && make -j $(nproc) && make install`

* `sudo apt install virtualenvwrapper`

* `source /usr/local/bin/virtualenvwrapper.sh`

* `mkvirtualenv trekkpedia --python=\`which python3\``

* `pip install -r requirements.txt`

DATABASE AND RUNSERVER

* `sudo add-apt-repository ppa:ubuntugis/ubuntugis-unstable`

* `sudo apt update`

* `sudo apt install -y postgresql postgresql-contrib postgis`

* `sudo su postgres`

* `createuser -d -SRP $USERNAME$`

* `createdb -O $DBNAME$ $USERNAME$`

* `sudo su postgres`

* `psql -d $DBNAME$`

* `$DBNAME$=# CREATE EXTENSION postgis;`

* `$DBNAME$=# \q`

* `su`

* `python manage.py migrate`

* `DATABASE_URL=postgis://$USERNAME$:$PASSWORD$@$HOST$:$PORT$/$DBNAME$ python manage.py runserver`, then open another tab on terminal

FRONTEND

* `sudo apt install npm node`

* `cd frontend`

* `npm i`

* `npm run watch`