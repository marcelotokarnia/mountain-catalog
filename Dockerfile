FROM marcelotokarnia/trackpedia:0.0.25

MAINTAINER Marcelo Tokarnia <marcelo.tokarnia@gmail.com>

WORKDIR /app

ADD requirements.txt /app
RUN pip install --trusted-host pypi.python.org -r requirements.txt

ADD . /app

COPY docker/nginx.conf /etc/nginx/sites-enabled
COPY docker/uwsgi.ini uwsgi.ini
COPY docker/trekkpedia.crt trekkpedia.crt
COPY docker/trekkpedia.key trekkpedia.key
COPY docker/uwsgi_params /uwsgi/uwsgi_params

ENTRYPOINT ["docker/entrypoint.sh"]
