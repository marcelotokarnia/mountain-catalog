# Trekkpedia

## How to hack locally (Explained)

Disclaimer:

This setup instructions are focused on Linux users, if you are using MacOs or Windows, you might need to adapt.

### A. Set Up your Python Virtualenv

1. Choose and download

    First, setup your favorite virtualenv. I recommend [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/).

2. Create and activate your virtualenv.

    If you are using virtualenvwrapper. You might need to source it on your terminal first.

    `source /usr/local/bin/virtualenvwrapper.sh`

    To create you virtual environment just prompt:

    ``mkvirtualenv {your_venv_name} --python=`which python3\` ``

    It will activate automatically. But, for future reference, when you already have an environment set up, to activate it you prompt:

    `workon {your_venv_name}`

    And to deactivate it, just prompt:

    `deactivate`

### B. Python requirements

With your virtualenv set up and activated, to download all project requirements, on your project root folder:

`pip install -r requirements.txt`

### C. Frontend requirements

You will need [npm](https://www.npmjs.com/) and [Node](https://nodejs.org).

You might get those by

`sudo apt install npm nodejs`

Then change directory into frontend folder:

`cd frontend`

And install project requirements locally:

`npm i`

### D. Raise your node server

You need this to server webpack automagically bundled assets after each change on frontend files

`npm run watch`

### E. Create the database

First, you will need postgres

`sudo apt-get update`

`sudo apt-get install -y postgresql postgresql-contrib`

Then, you will need postgis extension

`sudo add-apt-repository ppa:ubuntugis/ubuntugis-unstable`

`sudo apt-get update`

`sudo apt-get install -y postgis`

Now, set your postgres user and database:

`sudo su postgres`

`createuser -d -SRP $USERNAME$` (any username you wish to create, you will be prompted a $PASSWORD$)

`createdb -O $DBNAME$ $USERNAME$` (again, any dbname you wish to create, repeat the username above, it will be the owner of the database)

Now, database and user created you will need to install postgis extension on your database

`psql -d $DBNAME$` (to connect to your DB)

`$DBNAME$=# CREATE EXTENSION postgis;`

To verify the installation:

`$DBNAME$=# SELECT PostGIS_version();`

You should see something like:

```
Output
            postgis_version
---------------------------------------
 2.2 USE_GEOS=1 USE_PROJ=1 USE_STATS=1
(1 row)
```

All set, to disconnect from database:

`$DBNAME$=# \q`

Then switch back to your user:

`exit`

### F. Migrate database schema

Back at root folder

`cd ..`

`python manage.py migrate`

### G. Populate Database

Now your database is migrated, you will need to populate it, some samples can be written by:

`python manage.py crawl_peakware --start 1 --stop 100`

Don't worry about duplicates, this command will only update your entities.

In case your database already have some (or all) the data, the script will not duplicate them.

### H. Raise your Django local server

You will need a special environment variable now:

`export DATABASE_URL=postgis://$USERNAME$:$PASSWORD$@$HOST$:$PORT$/$DBNAME$` (refer to section E to modify this variables between $, your $HOST$ should be `localhost` and $PORT$ should be `5432` unless you made some extra custom configurations)

Hint: you might want to export this command to an `.env` file.

`python manage.py runserver`

or you might even want to alias something like:

`DATABASE_URL=postgis://$USERNAME$:$PASSWORD$@$HOST$:$PORT$/$DBNAME$ python manage.py runserver`